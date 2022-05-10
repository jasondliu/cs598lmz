import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------
class CsvFile:
    """
    """
    def __init__(self, filename, mode='r', encoding='utf-8', delimiter=',', quotechar='"'):
        """
        """
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.file = None
        self.reader = None
        self.writer = None
        self.open()

    def open(self):
        """
        """
        if self.mode == 'r':
            self.file = codecs.open(self.filename, self.mode, self.encoding, 'strict')
            self.reader = csv.reader(self.file, delimiter=self.delimiter, quotechar=self.quotechar)
        elif self.mode == 'w':
            self.file = codecs.open(self.filename, self.mode, self.encoding
