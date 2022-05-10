import io
# Test io.RawIOBase
class myraw(io.RawIOBase):
    def read(self, size=-1):
        pass
# Test io.BufferedIOBase
class mybuf(io.BufferedIOBase):
    def read(self, size=-1):
        pass

# Test io.TextIOBase
class mytext(io.TextIOBase):
    def read(self, size=-1):
        pass

# Test io.FileIO
class myfile(io.FileIO):
    def read(self, size=-1):
        pass

# Test io.BytesIO
class mybytes(io.BytesIO):
    def read(self, size=-1):
        pass

# Test io.StringIO
class mystring(io.StringIO):
    def read(self, size=-1):
        pass

# Test io.BufferedReader
class mybuf_reader(io.BufferedReader):
    def read(self, size=-1):
        pass

# Test io.BufferedWriter
class mybuf_writer(io.BufferedWriter):
    def write(self,
