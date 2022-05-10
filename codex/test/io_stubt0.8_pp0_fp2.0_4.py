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

#[PyPy 1.7.1 (1.7.1+dfsg-1)]$ python3 -c "import _io;print(_io.PyBUF_SIMPLE);print(_io.PyBUF_WRITABLE);print(_io.PyBUF_FORMAT)"
#0
#1
#8

#[PyPy 1.7.1 (1.7.1+dfsg-1)]$ python3 -c "with open('xxx','rb') as f:print(f.readinto(bytearray(b'\xff')).__buffer__)"
#<read-only buffer for 0x1fc80e0, size 1, offset 0 at 0x1fc7978>


def get_buf():
    global view
    return view

#[PyPy 1.7.1 (1.7.1+dfsg-1)]$ python3 -c "from X import *;assert(get_buf()[0]==0xff)"
