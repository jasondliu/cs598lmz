import io
# Test io.RawIOBase.readall()

class MyRawIO(io.RawIOBase):
    def readall(self):
        return b'yay!'
MyRawIO().readall()

class MyRawIOWithRead(io.RawIOBase):
    def read(self, size):
        if size >= 4:
            return b'yay!'
        return b''

try:
    MyRawIOWithRead().readall()
except AttributeError as e:
    # This is ok, since read() isn't defined.
    pass
else:
    raise Exception("expected test of undefined read() to fail")

class MyRawIOWithReadinto(io.RawIOBase):
    def readinto(self, buf):
        if len(buf) >= 4:
            buf[:4] = b'yay!'
            return 4
        return 0

try:
    MyRawIOWithReadinto().readall()
except AttributeError as e:
    # This is ok, since readinto() isn't defined.
    pass
else:
    raise Exception("expected test of undefined readinto
