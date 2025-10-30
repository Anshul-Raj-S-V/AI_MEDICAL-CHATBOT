# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS
from dotenv import load_dotenv
from pydub import AudioSegment

load_dotenv()

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is Ai with Hassan!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.getenv("ELEVEN_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel (default)
        model_id="eleven_turbo_v2",
        text=input_text
    )

    elevenlabs.save(audio, output_filepath)
text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")
#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 
import subprocess
import platform
#Step2: Use Model for Text output to Voice

def text_to_speech_with_gtts(input_text, output_filepath):
    """
    Convert text to speech using Google TTS (gTTS),
    save as MP3, convert to WAV, and auto-play based on OS.
    """
    language = "en"

    # Generate speech and save as MP3
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

    # Convert MP3 to WAV for playback (some OS require WAV)
    wav_filepath = output_filepath.replace(".mp3", ".wav")
    AudioSegment.from_mp3(output_filepath).export(wav_filepath, format="wav")

    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', wav_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run([
                'powershell', '-c',
                f'(New-Object Media.SoundPlayer "{wav_filepath}").PlaySync();'
            ])
        elif os_name == "Linux":
            subprocess.run(['aplay', wav_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"❌ Error while trying to play the audio: {e}")

# Example test
# text_to_speech_with_gtts("Hi, this is AI with Hassan. Autoplay testing!", "gtts_testing_autoplay.mp3")


from pydub import AudioSegment
import subprocess, platform, os
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.getenv("ELEVEN_API_KEY")

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    if not input_text or not input_text.strip():
        raise ValueError("❌ No valid input text provided for ElevenLabs TTS.")

    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio_stream = client.text_to_speech.convert(
        voice_id="21m00Tcm4TlvDq8ikWAM",  # Rachel
        model_id="eleven_turbo_v2",
        text=input_text
    )

    # ✅ Write streamed audio to file
    with open(output_filepath, "wb") as f:
        for chunk in audio_stream:
            f.write(chunk)

    # ✅ Convert MP3 → WAV
    wav_path = output_filepath.replace(".mp3", ".wav")
    AudioSegment.from_mp3(output_filepath).export(wav_path, format="wav")

    # ✅ Auto play depending on OS
    os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_path}").PlaySync();'])
        elif os_name == "Darwin":
            subprocess.run(['afplay', wav_path])
        elif os_name == "Linux":
            subprocess.run(['aplay', wav_path])
    except Exception as e:
        print(f"An error occurred while playing audio: {e}")

    return wav_path
