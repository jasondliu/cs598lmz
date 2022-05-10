import _struct
# Test _struct.Struct
_struct.Struct('i').pack(1)
# Test cpyext.struct
cpyext.Struct('i').pack(1)
# Test cpyext.bufstruct
cpyext.BUFStruct('i').pack(1)


# Test file()
thefile = file(__file__)
thefile.read()


# Test FileIO() for file-like Python objects
class PyFileLike(object):
    def __init__(self):
        self.written = ''
        self.seekpos = 0

    def write(self, s):
        self.written += s

    def seek(self, pos, whence=0):
        if whence == 0:
            self.seekpos = pos
        elif whence == 1:
            self.seekpos += pos
        elif whence == 2:
            self.seekpos = len(self.written) + pos

    def tell(self):
        return self.seekpos


# Test FileIO() with wraparound
import _io
wrapped = cpyext.PyObject_AsFileDescriptor(_io.Bytes
