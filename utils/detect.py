import whisper


def generate_text(file):
    model = whisper.load_model('small')
    text = model.transcribe(file)

    with open('content.txt', 'w') as f:
        f.write(text['text'])
