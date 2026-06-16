import fitz

class WordExtract:


    def __init__(self, file_path):
        self.file_path = file_path
        self.doc = fitz.open(self.file_path)
        self.text = self.doc[0].get_text()

