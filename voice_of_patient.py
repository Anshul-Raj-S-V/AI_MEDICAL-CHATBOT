# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1: Setup Audio recorder (ffmpeg & portaudio)
# ffmpeg, portaudio, pyaudio
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from dotenv import load_dotenv
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()
def record_audio(file_path="patient_voice_test.mp3", timeout=20, phrase_time_limit=None):
    """
    Record audio from microphone and save as MP3.
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("🎙️ Adjusting for ambient noise... Please wait 1 sec.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("🗣️ Start speaking now... Recording will auto-stop after silence or limit.")

            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("✅ Recording complete.")

            # Convert the audio to MP3 format
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")

            logging.info(f"💾 Audio saved to {file_path}")
            return file_path

    except Exception as e:
        logging.error(f"❌ Error while recording audio: {e}")
        return None
    record_audio(file_path=audio_filepath)

#Step2: Setup Speech to text–STT–model for transcription
import os
from groq import Groq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
stt_model="whisper-large-v3"

def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)

    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model=stt_model,
            file=audio_file,
            language="en"
        )

    return transcription.text


