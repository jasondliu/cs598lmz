import codecs
codecs.register_error('ignore', codecs.ignore_errors)

class File(object):
    def __init__(self, filename):
        self.filename = filename
        self.data = None
        self.size = 0
        self.read()

    def read(self):
        try:
            with codecs.open(self.filename, encoding='utf-8', errors='ignore') as f:
                self.data = f.read()
                self.size = len(self.data)
        except IOError:
            raise

    def write(self, data):
        with codecs.open(self.filename, 'w', encoding='utf-8') as f:
            f.write(data)
            f.flush()

class FileManager(object):
    def __init__(self, files):
        self.files = files
        self.data = []
        self.size = 0
        self.read()

    def read(self):
        try:
            for f in self.files:
                self.data.append(File(f).data)
                self.size += len
