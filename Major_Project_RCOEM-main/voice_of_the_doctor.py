# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi This is Nayan Pillewar from RCOEM!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs (UPDATED)
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")  # Changed from ELEVEN_API_KEY

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    if not ELEVENLABS_API_KEY:
        print("Error: ELEVENLABS_API_KEY not found in environment variables")
        return
    
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    # Use the new text_to_speech.convert() method with correct voice ID
    audio = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam voice ID (reliable)
        output_format="mp3_44100_128",
        text=input_text,
        model_id="eleven_turbo_v2"
    )
    
    # Save the audio
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    print(f"Audio saved to {output_filepath}")

#text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3")

'''
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is atharva raut!"
text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVEN_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_44100_128",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)

text_to_speech_with_elevenlabs_old(input_text, output_filepath="elevenlabs_testing.mp3") 
'''
#Step2: Use Model for Text output to Voice

import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            #subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
            subprocess.run(['powershell', '-c', f'Start-Process "{output_filepath}"'], check=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text="Hi this is Nayan Pilllewar, autoplaytesting it is! with gTTS model."
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.wav")


import subprocess
import platform
from elevenlabs.client import ElevenLabs

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    
    # Use the new text_to_speech.convert() method
    audio = client.text_to_speech.convert(
        voice_id="TC0Zp7WVFzhA8zpTlRqV",  # Aria voice ID
        output_format="mp3_22050_32",
        text=input_text,
        model_id="eleven_turbo_v2"
    )
    
    # Save the audio using chunks
    with open(output_filepath, "wb") as f:
        for chunk in audio:
            f.write(chunk)
    
    # Autoplay the audio
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            # Use Start-Process for MP3 files (fixed from your gTTS solution)
            #subprocess.run(['powershell', '-c', f'Start-Process "{output_filepath}"'], check=True)
            subprocess.run(['powershell', '-c', f'Invoke-Item "{output_filepath}"'], check=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['mpg123', output_filepath])  # Use mpg123 for MP3
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")





















'''

def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.generate(
        text= input_text,
        voice= "Aria",
        output_format= "mp3_22050_32",
        model= "eleven_turbo_v2"
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_testing_autoplay.mp3")
'''