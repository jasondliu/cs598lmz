import io
# Test io.RawIOBase.readall()
class readall_io(io.RawIOBase):
    def readall(self):
        return b'bytes'
readall_io().readall()

# Test io.BytesIO.readall()
class readall_io(io.BytesIO):
    def readall(self):
        return b'bytes'
readall_io().readall()

# Test io.BufferedIOBase.readall()
class readall_io(io.BufferedIOBase):
    def readall(self):
        return b'bytes'
readall_io().readall()

# Test io.BufferedRandom.readall()
class readall_io(io.BufferedRandom):
    def readall(self):
        return b'bytes'
