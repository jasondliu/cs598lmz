import threading
threading.stack_size(67108864)

class PdfDataProcessor(object):
    """Processor for the data of a PDF file"""
    def __init__(self, pdf_file_path, pdf_file_name, pdf_file_text):
        self.pdf_file_path = pdf_file_path
        self.pdf_file_name = pdf_file_name
        self.pdf_file_text = pdf_file_text

    def get_file_name(self):
        """Returns the name of the file"""
        return self.pdf_file_name

    def get_file_text(self):
        """Returns the text of the file"""
        return self.pdf_file_text

    def get_file_path(self):
        """Returns the path of the file"""
        return self.pdf_file_path

class PdfDataProcessorFactory(object):
    """Factory for creating processors for the data of PDF files"""
