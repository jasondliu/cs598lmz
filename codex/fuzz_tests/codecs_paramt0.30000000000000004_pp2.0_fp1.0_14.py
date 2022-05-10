import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
#
#
class File(object):
    def __init__(self, path, mode='rb', encoding='utf-8', errors='strict'):
        self.path = path
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.file = None
        self.lines = None
        self.line_number = 0

    def __enter__(self):
        self.file = codecs.open(self.path, self.mode, self.encoding, self.errors)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        self.line_number += 1
        return next(self.file)

    def read(self):
        self.lines = self.file.readlines()
        return self.lines

    def write(self, line):
        self.file.write(line
