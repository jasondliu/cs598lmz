import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def read(self, size=-1):
        return b''
    def write(self, b):
        return len(b)

try:
    io.RawIOBase()
except TypeError:
    print('SUCCESS: io.RawIOBase fails')
else:
    print('FAILURE: io.RawIOBase fails')

try:
    MyRawIO()
except TypeError:
    print('SUCCESS: MyRawIO fails')
else:
    print('FAILURE: MyRawIO fails')

try:
    MyRawIO().read()
except TypeError:
    print('SUCCESS: MyRawIO.read fails')
else:
    print('FAILURE: MyRawIO.read fails')

try:
    MyRawIO().write(b'a')
except TypeError:
    print('SUCCESS: MyRawIO.write fails')
else:
    print('FAILURE: MyRawIO.write fails')

