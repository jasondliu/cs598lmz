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
print("resume:", view)
del view

import cStringIO
f = cStringIO.StringIO("some data")
f.write("some more data")
f.seek(0)
print("cStringIO:", f.read())
del f

import StringIO
f = StringIO.StringIO("some data")
f.write("some more data")
f.seek(0)
print("StringIO:", f.read())
del f

# test https://github.com/micropython/micropython/issues/2568
import sys
print("sys.stdin:", sys.stdin.readline())

import uos
print_exc = uos.dupterm_notify
uos.dupterm_notify(lambda *args: None)
print("stdout:", sys.stdout.write("test\n"))
print("stderr:", sys.stderr.write("test\n"))
uos.dupterm_notify(print_exc)

class MyIOBase(io.IOBase):
    pass
