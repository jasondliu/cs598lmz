import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def readable(self):
        return True
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n

import sys
import io

f = File(sys.stdin.buffer)
print(f.read())

import sys
import io

f = File(sys.stdin.buffer)
print(f.read())

import sys
import io

f = File(sys.stdin.buffer)
print(f.read())

import sys
import io

f = File(sys.stdin.buffer)
print(f.read())

import sys
import io

f = File(sys.stdin.buffer)
print(f.
