import codecs
codecs.register_error('strict', codecs.ignore_errors)

#
# 
#

class File(object):
    def __init__(self, filename, mode='r', encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None
        self.open()

    def open(self):
        self.file = codecs.open(self.filename, self.mode, self.encoding, 'strict')

    def close(self):
        self.file.close()

    def read(self):
        return self.file.read()

    def write(self, data):
        self.file.write(data)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

#
# 
#

class FileReader(File):
    def __init__(self, filename, encoding='utf-8'):
        super(FileReader, self).__init__(filename, 'r', encoding
