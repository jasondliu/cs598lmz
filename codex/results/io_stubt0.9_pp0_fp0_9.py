import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
assert not hasattr(view, "__len__")

f = io.BufferedReader(File())
f.read(1)
assert hasattr(view, "__len__")

f = io.BufferedReader(File())
f.peek(1)
del f
assert not hasattr(view, "__len__")

f = io.BufferedReader(File())
f.peek(1)
assert hasattr(view, "__len__")

f = io.BufferedReader(io.StringIO())
f.read(1)
assert f.peek(1) is None
assert f.read() == ""

# Issue 14365
import os
from os import path as osp
from io import TextIOWrapper
from tempfile import TemporaryDirectory
with TemporaryDirectory() as tmpdir:
    dotdot = osp.join(tmpdir, '..', tmpdir)
    io.open(dotdot, 'w', encoding='utf8').close()
    assert io.open(dotdot, encoding='utf8').encoding == 'utf8'
