import io
# Test io.RawIOBase
import io

class MyRawIO(io.RawIOBase):
    def read(self, size=-1):
        pass

io.RawIOBase.read()
io.RawIOBase.read()

# Test io.BufferedIOBase
import io

class MyBufferedIO(io.BufferedIOBase):
    def read(self, size=-1):
        pass

io.BufferedIOBase.read()
io.BufferedIOBase.read()

# Test io.StringIO
import io

class MyStringIO(io.StringIO):
    def read(self, size=-1):
        pass

io.StringIO.read()
io.StringIO.read()
