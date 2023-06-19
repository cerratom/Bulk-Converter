# Bulk-Converter

# Video to Text Converter

This script is designed to convert video (MP4) files into text (TXT) files using speech recognition. It utilizes the `moviepy` and `whisper` libraries to perform the conversion.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- `moviepy`
- `whisper`

You can install these libraries using the following command:

```shell
pip install moviepy whisper
```

## Usage

1. Place your video files in the designated folder.

2. Run the script by executing the following command:

```shell
python script.py
```

3. The script will perform the following steps:

   a. Convert MP4 files to WAV format using the `convert_mp4_to_wav` function.

   b. Convert the audio files to text using the `convert_audio_to_text` function and the pre-trained `whisper` model.

   c. Save the transcribed text in separate TXT files.

4. The converted text files will be saved in the specified `Text` folder.

## Functions

The script contains two main functions:

### `convert_mp4_to_wav(mp4_file)`

This function converts an MP4 video file to WAV audio format. The resulting WAV file will be saved in the `Audio` folder with the same name as the input MP4 file but with the extension `.wav`. The audio codec used for the WAV file is `pcm_s16le` (16-bit uncompressed audio with little-endian byte order).

Example usage: `convert_mp4_to_wav('path/to/video.mp4')`

### `convert_audio_to_text(audio_file)`

This function converts an audio file to text using a pre-trained speech recognition model provided by the `whisper` library. The supported audio formats can be found in the `whisper` library documentation. The function returns the transcribed text obtained from the audio.

Example usage: `convert_audio_to_text('path/to/audio.wav')`

## Configuration

You can modify the following variables in the script to suit your needs:

- `folder_path`: Path to the folder containing the MP4 video files.
- `audio_folder`: Path to the folder where the converted audio files will be saved.
- `text_folder`: Path to the folder where the resulting text files will be saved.

Note: The script assumes that the `Audio` and `Text` folders already exist. If they don't, the script will create them automatically.

## License

This script is provided under the [MIT License](https://opensource.org/licenses/MIT).

Please refer to the license file for more information.
