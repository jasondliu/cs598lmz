import codecs
codecs.register_error("strict", codecs.ignore_errors)

class File(object):
    def __init__(self, filename, mode="r"):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.__enter__()

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()

    def read(self, size=None):
        return self.file.read(size)

    def readline(self):
        return self.file.readline()

    def readlines(self):
        return self.file.readlines()

    def write(self, data):
        self.file.write(data)

    def writelines(self, data):
        self.file.writelines(data)

    def flush(self):
        self.file.flush()

    def close(self):
        self.file.close()

    def seek(self, pos):
        self
