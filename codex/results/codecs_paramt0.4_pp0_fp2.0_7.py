import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Parser(object):
    def __init__(self, path):
        self.path = path
        self.file = codecs.open(path, encoding='utf-8', errors='strict')
        self.line = self.file.readline()
        self.line_number = 0

    def __iter__(self):
        return self

    def next(self):
        self.line_number += 1
        line = self.line
        self.line = self.file.readline()
        if not line:
            raise StopIteration
        return line
