import pytube

video = 'https://www.youtube.com/watch?v=-LIIf7E-qFI'
data = pytube.YouTube(video)

audio = data.streams.get_audio_only()
audio.download()
