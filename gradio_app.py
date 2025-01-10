import gradio_app as gr
from transformers import pipeline
import os

# Load the Whisper ASR pipeline
asr_pipeline = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")

# Directory to save uploaded audio files
SAVE_DIR = "uploaded_audio"
os.makedirs(SAVE_DIR, exist_ok=True)

def transcribe_audio(audio):
    # Save the audio file locally
    audio_path = os.path.join(SAVE_DIR, os.path.basename(audio))
    os.rename(audio, audio_path)
    
    # Perform transcription using Whisper
    transcription = asr_pipeline(audio_path)["text"]
    return transcription, audio_path

# Define the Gradio interface
interface = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(),
    outputs=["text"],
    title="Automatic Speech Recognition with Whisper",
    description="Upload an audio file to see its transcription. The audio file will also be saved locally."
)

# Launch the Gradio app
interface.launch()
