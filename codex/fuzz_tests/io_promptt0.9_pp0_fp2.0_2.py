import io
# Test io.RawIOBase.readinto()
r = io.BytesIO(b'*' * 10)
buf = bytearray(5)
r.readinto(buf)
r.readinto1(buf)

import os
# Test os.PathLike.readinto()
f = os.fsencode(__file__)
buf = bytearray(1)
os.readinto(f, buf)

# Test os.PathLike.write()
f = os.fsencode(__file__)
os.write(f, b'foo')
os.write(f, bytearray(b'foo'))

class Foo(int):
    def __init__(self, x):
        self.x = x

    def __index__(self):
        return self.x

import pandas as pd
a = pd.DataFrame([Foo(0), Foo(1)])
b = a < Foo(2)

class Cell:
    def __setattr__(self, key, value):
        if key == '__dict__':
            super().
