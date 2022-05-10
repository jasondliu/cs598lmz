import io
class File(io.RawIOBase):
    def __init__(self, file_):
        self.file = file_

    def readinto(self, b):
        return self.file.readinto(b)

    def read(self, n=-1):
        return self.file.read(n)

    def write(self, b):
        return self.file.write(b)

class file(object):
    '''
    A file wrapper that seeks to the end of the file on __enter__
    Useful for appending to a file.
    '''
    def __init__(self, file_name, *args, **kwargs):
        self.file_name = file_name
        self.args = args
        self.kwargs = kwargs

    def __enter__(self):
        self.file = open(self.file_name, *self.args, **self.kwargs)
        self.file.seek(0, io.SEEK_END)
        return self.file

    def __exit__(self, *args):
        self.file.close()

class atomic_
