# Import the necessary libraries

import os
import whisper
from moviepy.editor import VideoFileClip
from glob import glob

# Define a function that converts video files into audio files.

def convert_mp4_to_wav(mp4_file):
    """Convert an MP4 video file to WAV audio format. This function requires the `moviepy` library to be installed. 
    The converted WAV file will be saved in the 'Audio' folder with the same name as the input MP4 file but with the extension '.wav'. 
    The audio codec used for the WAV file is 'pcm_s16le', which represents uncompressed 16-bit audio with little-endian byte order. 
    If the specified MP4 file is not found, a FileNotFoundError will be raised. 
    If an error occurs during the conversion process, an OSError will be raised. 
    Example usage: convert_mp4_to_wav('path/to/video.mp4')"""
  
    video_clip = VideoFileClip(mp4_file)
    wav_filename = os.path.splitext(os.path.basename(mp4_file))[0] + '.wav'
    output_folder = 'Audio'
    os.makedirs(output_folder, exist_ok=True)
    wav_path = os.path.join(output_folder, wav_filename)
    video_clip.audio.write_audiofile(wav_path, codec='pcm_s16le')

# Define a function that converts video files into audio files.

def convert_audio_to_text(audio_file):
    """Convert an audio file to text using a pre-trained speech recognition model. This function requires the 'whisper' library to be installed. 
    The function utilizes a pre-trained model called 'base' for speech recognition. The audio file can be in various formats supported by the 'whisper' library. 
    If the specified audio file is not found, a FileNotFoundError will be raised. 
    If an error occurs during the transcription process, a whisper.WhipserException will be raised. 
    The function returns the transcribed text obtained from the audio. 
    Example usage: convert_audio_to_text('path/to/audio.wav')"""
    model = whisper.load_model("base")
    result = model.transcribe(audio_file, fp16=False)
    return result    

# Path to the folder containing MP4 files
folder_path = 'Video'

# Get a list of MP4 files in the folder
mp4_files = glob(os.path.join(folder_path, '*.mp4'))

for mp4_file in mp4_files:
    convert_mp4_to_wav(mp4_file)
    
# Path to the folder containing audio files
audio_folder = 'Audio'

# Path to the folder where text files will be saved
text_folder = 'Text'
os.makedirs(text_folder, exist_ok=True)

# Path to the whisper model
model = whisper.load_model("base")
   
# Get a list of audio files in the audio folder
audio_files = glob(os.path.join(audio_folder, '*.wav'))

# Calls the function to convert wav files to txt using whisper for each file in the audio folder and saves it to the text folder 
for audio_file in audio_files:
    result = convert_audio_to_text(audio_file)

    # Create the text file path with the same name as the audio file
    text_file = os.path.splitext(os.path.basename(audio_file))[0] + '.txt'
    text_path = os.path.join(text_folder, text_file)

    # Save the text to the text file
    with open(text_path, 'w') as file:
        file.write(result["text"])