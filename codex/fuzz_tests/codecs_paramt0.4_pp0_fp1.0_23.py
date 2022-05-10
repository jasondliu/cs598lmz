import codecs
codecs.register_error('strict', codecs.ignore_errors)

class File:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.size = os.path.getsize(path)
        self.mtime = os.path.getmtime(path)
        self.mimetype = mimetypes.guess_type(path)[0]
        self.content = None
        self.encoding = None
        self.lines = None

    def __str__(self):
        return '<File %s>' % self.path

    def __repr__(self):
        return self.__str__()

    def read(self):
        if self.content is None:
            with open(self.path, 'rb') as f:
                self.content = f.read()
        return self.content

    def read_lines(self):
        if self.lines is None:
            with open(self.path, 'rb') as f:
                self.lines = f.read
