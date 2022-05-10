import codecs
codecs.register_error('ignore_surrogates', codecs.ignore_errors)

class TextFile(object):
    def __init__(self, filepath, encoding='utf-8', errors='ignore', newline=None):
        self.filepath = filepath
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.file = None
        self.lineno = 0
        self.line = None
        self.column = None

    def __enter__(self):
        self.file = codecs.open(self.filepath, 'r', encoding=self.encoding, errors=self.errors, newline=self.newline)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        self.line = self.file.readline()
        if self.line:
            self.lineno += 1
            self.column = 1
            return self.
