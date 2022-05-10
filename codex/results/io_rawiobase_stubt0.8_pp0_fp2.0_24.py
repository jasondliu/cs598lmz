import io
class File(io.RawIOBase):
    pass
class FileReader(File):
    def read(self):
        return 1
    def close(self):
        pass

def noncompliant_func(file):
    if file.closed:
        raise ValueError
    file.read()
    file.close()

def compliant_func(file):
    if isinstance(file, FileReader):
        file.read()
        file.close()
    else:
        raise ValueError
