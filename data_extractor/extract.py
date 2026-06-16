import fitz

class DataExtract:
    """
    A class to do the extraction and from pdfs.

    Attributes"
        self.file_path: file path to the pdf within the folder
        self.doc: reader for the pds utilizing pymupdf
        self.text: indexes pymupdf and gets text

    Methods:
        
    """

    def __init__(self, file_path):
        self.file_path = file_path
        self.doc = fitz.open(self.file_path)
        self.text = self.doc[0].get_text()

