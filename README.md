## Getting Started

Follow the steps below to set up and run the project on your local machine.

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
