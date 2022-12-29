import pytube
from utils import detect
from utils import summarize

video = 'https://youtu.be/aZRS8BQc7cY'
data = pytube.YouTube(video)

audio = data.streams.get_audio_only()
audio.download()

detect.generate_text(audio.default_filename)
summarize.generate_summary("content.txt", 2)
