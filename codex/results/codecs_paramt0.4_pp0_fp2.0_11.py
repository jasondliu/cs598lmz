import codecs
codecs.register_error('strict', codecs.ignore_errors)

class File(object):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        try:
            self.file = codecs.open(name, mode, encoding='utf-8', errors='strict')
        except IOError:
            self.file = None
            print('File not found:', name)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.file.close()

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            raise StopIteration
        return line

    def write(self, string):
        self.file.write(string)

    def read(self):
        return self.file.read()

    def readline(self):
        return self.file.readline()

class Path(object):
    def __init__(self, path):

