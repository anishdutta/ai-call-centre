import whisper

class Whisper_Service:

    def __init__(self):
        self.audioPath = "./audio/audio.mp3"
        self.model = whisper.load_model("base")


    # Transcribe audio file to english
    # Todo:
    # [1] Hindi Support needed to be added
    def transcribe(self)->str:
        result = self.model.transcribe(self.audioPath)
        return result["text"]
