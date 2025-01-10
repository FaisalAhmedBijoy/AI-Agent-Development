import os
import gradio as gr
from scipy.io.wavfile import write
from datetime import datetime

# Function to process and save the recorded audio
def save_audio(audio):
    if audio is None:
        return "No audio provided!", "N/A", "N/A", "N/A"

    # Create a directory to store audio files
    save_dir = "recorded_audios"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Extract sampling rate and audio array
        sampling_rate, audio_array = audio

        # Generate a unique filename based on timestamp
        filename = f"{save_dir}/audio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"

        # Save the audio file using scipy
        write(filename, sampling_rate, audio_array)

        # Calculate audio duration
        duration = len(audio_array) / sampling_rate

        # Return detailed information
        filename_str = f"Audio saved to: {filename}"
        sampling_rate_str = f"Sampling Rate: {sampling_rate} Hz"
        duration_str = f"Duration: {duration:.2f} seconds"
        file_size_str = f"File Size: {os.path.getsize(filename) / 1024:.2f} KB"
        return filename_str, sampling_rate_str, duration_str, file_size_str

    except Exception as e:
        # Return error details in case of failure
        return f"Error: {str(e)}", "N/A", "N/A", "N/A"


if __name__ == "__main__":
    app = gr.Interface(
        fn=save_audio,
        inputs=gr.Audio(),
        outputs=[
            gr.Textbox(label="File Path"),
            gr.Textbox(label="Sampling Rate"),
            gr.Textbox(label="Audio Duration"),
            gr.Textbox(label="File Size")
        ],
        title="Microphone Audio Recorder",
        description=(
            "Record audio using your microphone or upload an audio file. "
            "This app saves the audio to your local disk and displays its details."
        ),
    )

    app.launch()
