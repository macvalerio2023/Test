from flask import Flask, render_template, request
from deepgram import DeepgramClient, PrerecordedOptions
import os
import webview

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Replace with your Deepgram API key
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY", "YOUR_DEEPGRAM_API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        try:
            deepgram = DeepgramClient(DEEPGRAM_API_KEY)

            with open(filepath, "rb") as audio:
                buffer_data = audio.read()

            payload = {
                "buffer": buffer_data,
            }

            options = PrerecordedOptions(
                model="nova-2",
                smart_format=True,
                utterances=True,
                puncutate="true",
                diarize=True if 'diarize' in request.form else False,
            )

            response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)

            transcription = response.results.channels[0].alternatives[0].transcript

        except Exception as e:
            transcription = f"Error: {e}"

        finally:
            os.remove(filepath)

        return render_template('index.html', transcription=transcription)

if __name__ == '__main__':
    webview.create_window('MP3 Transcription', app)
    webview.start()
