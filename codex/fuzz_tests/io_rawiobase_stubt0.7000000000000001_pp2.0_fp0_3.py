import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.f = open(filename)
    def read(self, n=-1):
        return self.f.read(n)
    def seek(self, n, whence=io.SEEK_SET):
        return self.f.seek(n, whence)
    def tell(self):
        return self.f.tell()
    def close(self):
        return self.f.close()
    def readable(self):
        return True

class Manager:
    def __init__(self):
        self.pipeline = Pipeline()
        self.pipeline.source(File("test_data.py"))
        self.pipeline.transform(self.transform_uppercase)
        self.pipeline.transform(self.transform_lowercase)
        self.pipeline.sink(File("test_data.py"))

    def transform_uppercase(self, chunk):
        return chunk.upper()

    def transform_lowercase(self, chunk):
        return chunk.lower()

    def run
