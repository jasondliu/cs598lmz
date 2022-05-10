import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------
#
#-------------------------------------------------------------------------------
class FileReader(object):
    def __init__(self, filename, encoding='utf-8'):
        self.filename = filename
        self.encoding = encoding
        self.file = None
        self.line = None
        self.lineno = 0
        self.open()

    def open(self):
        self.file = codecs.open(self.filename, 'r', self.encoding, 'strict')
        self.lineno = 0

    def close(self):
        self.file.close()

    def __iter__(self):
        return self

    def next(self):
        self.line = self.file.readline()
        if self.line:
            self.lineno += 1
            return self.line
        else:
            raise StopIteration()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

#-------------------------------------------------------------------------------
#
#
