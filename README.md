## Getting Started
Follow the steps below to set up and run the project on your local machine.

<br>

### 1. Prerequisites
- Python 3.8 or later
- pip (Python package installer)

<br>

### 2. Installation
#### Clone the repository:
- ``` git clone https://github.com/ErayBD/finger-draw.git ```
#### Install the required Python packages:
- ``` cd finger-draw ```
- ``` pip install -r requirements.txt ```

<br>

### 3. Configuration
#### Set up your Google AI API Key:
- Obtain an API key from the Google Cloud Console.
- Replace the placeholder API key in the geminiConfig() function within main.py:
- ``` genai.configure(api_key="YOUR_API_KEY_HERE") ```

<br>

### 4. Running the Application
#### Start the Streamlit application:
- ``` streamlit run main.py ```

<br>

### 5. Using the Application
- ***Drawing:*** Use your *INDEX* finger to draw on the screen.
- ***Clearing the Screen:*** Hold up all *FIVE* fingers to clear the canvas.
- ***Sending Drawing to AI:*** Hold up your *THUMB*, *INDEX*, and *PINKY* fingers (while the other two fingers are down) to send the drawing to the AI for interpretation.

<br>

### 6. Project Screenshots
![1](https://github.com/user-attachments/assets/8b229d83-b98d-4eb6-a16b-ebe88715c72d)

<br>

![2](https://github.com/user-attachments/assets/08ca89ba-97e3-4d8c-bde0-cc332b599950)

<br>

![3](https://github.com/user-attachments/assets/a3fb5184-77de-4232-94f0-abf31b8391c2)

