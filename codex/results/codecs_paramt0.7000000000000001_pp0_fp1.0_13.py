import codecs
codecs.register_error("strict", codecs.ignore_errors)


class FileWriter:
    def __init__(self, filename, mode='w'):
        self.f = open(filename, mode)
        self.file_name = filename

    def write(self, content):
        self.f.write(content)

    def close(self):
        self.f.flush()
        self.f.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()


class FileReader:
    def __init__(self, filename, mode='r'):
        self.f = open(filename, mode)
        self.file_name = filename

    def read(self, size=None):
        return self.f.read(size)

    def readline(self):
        return self.f.readline()

    def readlines(self):
        return self.f.readlines()

    def close(self):
        self.f.close()

    def __enter__(self):
