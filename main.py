import cvzone
import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
import google.generativeai as genai
from PIL import Image
import streamlit as st

# This function detects hands in an image and returns information about fingers.
def getHandInfo(img):
    # "draw" parameter is set to True to visualize hand and finger detection.
    hands, img = detector.findHands(img, draw=True, flipType=True)

    # Check if any hands are detected
    if hands:
        hand = hands[0]  # Get the first detected hand
        lmList = hand["lmList"]  # Get the list of 21 landmarks of the first hand
        fingers = detector.fingersUp(hand)  # Count the number of fingers up for the first hand
        print(fingers)  # Print which fingers are up
        return fingers, lmList
    else:
        return None

# This function handles drawing operations based on the detected finger positions.
def draw(info, prev_pos, draw_canvas):
    fingers, lmList = info  # Get the values returned from the getHandInfo function
    current_pos = None

    # If only the index finger is up
    if fingers == [0, 1, 0, 0, 0]:
        current_pos = lmList[8][0:2]  # Get the x, y coordinates of the index finger tip

        if prev_pos is None:
            prev_pos = current_pos

        # Draw a line on the canvas from the previous position to the current position
        cv2.line(draw_canvas, current_pos, prev_pos, (255, 0, 255), 10)

    # If all fingers are up
    elif fingers == [1, 1, 1, 1, 1]:
        draw_canvas = np.zeros_like(img)  # Clear the drawing canvas

    return current_pos, draw_canvas

# This function sends the drawing on the canvas to the AI model and gets a response.
def sendToAI(model, canvas, fingers):
    questionText = "Describe what is drawn in pink on the screen. Solve it if it's a problem."  # Define the query for the model
    pil_image = Image.fromarray(canvas)  # Convert the canvas to a PIL image

    # If the finger configuration matches the specified pattern
    if fingers == [1, 1, 0, 0, 1]:
        # Ask the AI model to generate a response based on the question and image
        response = model.generate_content([questionText, pil_image])
        return response.text

# Configure the Streamlit UI.
def streamlitConfig():
    st.set_page_config(layout="wide")
    st.title("Camera")
    FRAME_WINDOW = st.image([])  # Placeholder for displaying the image
    st.title("Answer")
    output_text_area = st.subheader("")  # Create a title area for displaying the AI response

    return FRAME_WINDOW, output_text_area

# Configure the AI model.
def geminiConfig():
    genai.configure(api_key="YOUR_API_KEY_HERE")  # Set up the API key for the AI model
    model = genai.GenerativeModel('gemini-1.5-flash')  # Specify the version of the model to use
    return model

# Main program entry point
if __name__ == '__main__':

    # Initialize variables
    prev_pos = None
    draw_canvas = None
    canvas_combine = None
    output_text = None
    model = geminiConfig()  # Configure the AI model
    FRAME_WINDOW, output_text_area = streamlitConfig()  # Configure the Streamlit interface

    # Start the webcam and set its resolution
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        st.error("Could not open webcam. Please check if it is connected properly.")
        st.stop()  # Stops the Streamlit script execution
    else:
        cap.set(3, 1280)
        cap.set(4, 720)

    # Initialize the HandDetector class with specified parameters
    detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.5, minTrackCon=0.5)

    # Continuously capture frames from the webcam
    while True:
        # Capture each frame from the webcam
        success, img = cap.read()

        # Check if the frame was captured successfully
        if not success or img is None:
            st.error("Failed to capture image from webcam.")
            break  # Exit the loop if there's an issue with the webcam

        # Flip the image horizontally (mirror image)
        img = cv2.flip(img, 1)

        # Initialize the drawing canvas with black if it hasn't been created yet
        if draw_canvas is None:
            draw_canvas = np.zeros_like(img)
            canvas_combine = img.copy()

        # Get hand information
        info = getHandInfo(img)

        if info is not None:
            fingers, lmList = info
            print(fingers)
            prev_pos, draw_canvas = draw(info, prev_pos, draw_canvas)  # Call the draw function
            output_text = sendToAI(model, canvas_combine, fingers)  # Send the drawing to the AI model

        # Combine the original image with the drawing canvas and display it
        canvas_combine = cv2.addWeighted(img, 0.75, draw_canvas, 0.40, 1)
        FRAME_WINDOW.image(image=canvas_combine, channels="BGR")

        # If there is an output from the AI model, display it in the UI
        if output_text:
            output_text_area.text(output_text)

        # Keep the window open and update it for each frame; close when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources and close windows
    cap.release()
    cv2.destroyAllWindows()
