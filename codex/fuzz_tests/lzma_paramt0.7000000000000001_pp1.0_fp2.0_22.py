from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)

class PDFFile:
    def __init__(self,filename):
        self.filename=filename
        self.fp=open(filename,'rb')
        self.file_len=os.stat(filename).st_size
        self.header=self.fp.read(20)
        if self.header[0:5] != b'%PDF-':
            print('PDF file '+filename+' is not a PDF file!')
            exit(0)
        self.xref_start=self.fp.tell()
        self.xref_start=self.get_xref_start()
        self.xref_table=self.read_xref()
        self.trailer=self.read_trailer()
        self.find_catalog()
        self.read_catalog()
        self.find_pages()
        self.find_page_tree()
        self.find_text_pages()
        self.find_text_objects()
        self.find_text()

