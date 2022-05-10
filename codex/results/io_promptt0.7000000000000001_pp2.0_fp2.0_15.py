import io
# Test io.RawIOBase
class RawI(io.RawIOBase):

    def read(self, size=-1):
        ...
# Test io.FileIO
class FileI(io.FileIO):

    def read(self, size=-1):
        ...
# Test io.BufferedIOBase
class BufferedI(io.BufferedIOBase):

    def read(self, size=-1):
        ...
# Test io.TextIOBase
class TextI(io.TextIOBase):

    def read(self, size=-1):
        ...
# Test io.RawIOBase
class RawO(io.RawIOBase):

    def write(self, b):
        ...
# Test io.FileIO
class FileO(io.FileIO):

    def write(self, b):
        ...
# Test io.BufferedIOBase
class BufferedO(io.BufferedIOBase):

    def write(self, b):
        ...
# Test io.TextIOBase
class TextO(io.TextIOBase):

    def write(self, b):
        ...
# Test io.
