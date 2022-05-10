import io
# Test io.RawIOBase
class RawBytesIO(io.RawIOBase):
    def read(self, size=None):
        pass # ...
    def write(self, b):
        pass

try:
    io.RawIOBase()
except TypeError as e:
    print(e)
    print(RawBytesIO().read())

from io import BytesIO
# Test io.BufferedIOBase
class MyBytesIO(io.BufferedIOBase):
    def read(self, size=None):
        pass # ...
    def write(self, b):
        pass
    # ...
try:
    io.BufferedIOBase()
except TypeError as e:
    print(e)
    print(MyBytesIO().read())

# Test io.TextIOBase
class MyTextIO(io.TextIOBase):
    def read(self, size=None):
        pass # ...
    def write(self, b):
        pass

    def readline(self):
        pass
    def write(self, b):
        pass
    # ...
# try:
#    
