import PyPDF2
import processing_algorithms

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def read_pdf(file_name):
        pdfFileObj = open(file_name, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
        content = ""
        for i in range(pdfReader.numPages):
            content = content + " " + pdfReader.getPage(i).extractText()

        return content
