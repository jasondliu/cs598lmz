import io
# Test io.RawIOBase use
# /usr/lib/python3.4/io.py
import _io


class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        return b"\x00\x00\x00\x00"


print('io.RawIOBase')
# print(dir(io.RawIOBase).__contains__('closed'))
print(dir(io.RawIOBase) == dir(_io._RawIOBase))
print(dir(io.RawIOBase) == dir(io.BufferedIOBase))
print(dir(io.RawIOBase) == dir(MyRawIO))

print('-' * 20)
print('io.BufferedIOBase')
print(dir(io.BufferedIOBase))
print('-' * 20)
print('io.RawIOBase')
print(dir(io.RawIOBase))
