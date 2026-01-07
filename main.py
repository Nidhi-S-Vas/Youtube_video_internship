import os
import subprocess

#  Paths 
VIDEO_DIR = "input_video"
AUDIO_DIR = "extracted_audio"
CLEAN_AUDIO_DIR = "preprocessed_audio"

os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(AUDIO_DIR, exist_ok=True)
os.makedirs(CLEAN_AUDIO_DIR, exist_ok=True)

#  Step 1: Input YouTube URL 
youtube_url = "https://youtu.be/BqSxjmvXzzY?si=SegyoUOya3gFZC8g"

video_path = os.path.join(VIDEO_DIR, "video.mp4")
raw_audio_path = os.path.join(AUDIO_DIR, "raw_audio.wav")
clean_audio_path = os.path.join(CLEAN_AUDIO_DIR, "clean_audio.wav")

#  Step 2: Download Video 
print("Downloading video...")
subprocess.run([
    "yt-dlp",
    "-f", "mp4",
    "-o", video_path,
    youtube_url
], check=True)
print("Video downloaded successfully.")

#  Step 3: Extract Audio 
print("Extracting audio...")
subprocess.run([
    "ffmpeg",
    "-y",
    "-i", video_path,
    raw_audio_path
], check=True)
print("Audio extracted successfully.")

#  Step 4: Audio Preprocessing 
# Convert to mono and set sample rate to 16kHz
print("Preprocessing audio...")
subprocess.run([
    "ffmpeg",
    "-y",
    "-i", raw_audio_path,
    "-ac", "1",
    "-ar", "16000",
    clean_audio_path
], check=True)
print("Audio preprocessing completed.")

print("Completed successfully.")
