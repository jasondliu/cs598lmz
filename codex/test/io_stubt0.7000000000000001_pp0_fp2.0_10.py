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

view = None
"""

def test_gc_of_buffered_reader(pyversion):
    if pyversion < (3,):
        skip('no refcycle protection before Python 3')
    interp = get_interpreter(CPYTHON)
    interp.compile(pypy_code="""
