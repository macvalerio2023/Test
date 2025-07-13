# MP3 Transcription Web App

This web application transcribes MP3 audio files into text, with an option for speaker diarization.

## Setup

1.  **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Set your Deepgram API key:**

    This application uses the Deepgram API for transcription. You will need to get an API key from [Deepgram](https://deepgram.com/).

    You can set your API key as an environment variable:

    ```bash
    export DEEPGRAM_API_KEY="YOUR_DEEPGRAM_API_KEY"
    ```

    Alternatively, you can replace `"YOUR_DEEPGRAM_API_KEY"` directly in the `app.py` file.

## Running the Application

1.  **Start the Flask server:**

    ```bash
    flask run
    ```

2.  **Open your web browser and go to:**

    [http://127.0.0.1:5000](http://127.0.0.1:5000)

## How to Use

1.  Click the "Choose File" button to select an MP3 file from your computer.
2.  If you want to enable speaker diarization (to distinguish between different speakers), check the "Enable Speaker Diarization" box.
3.  Click the "Transcribe" button.
4.  The transcription will appear on the page.
