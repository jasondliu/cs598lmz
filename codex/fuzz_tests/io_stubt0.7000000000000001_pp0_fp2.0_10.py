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
    def make_file_obj():
        import _io
        # this is a simplified version of a CPython function
        return _io.FileIO(0, mode='rb', closefd=False, opener=lambda: None)

    def make_buffered_reader(bufsize=0):
        # this is a simplified version of a CPython function
        from _io import BufferedReader
        f = make_file_obj()
        return BufferedReader(f, bufsize)

    def main():
        f = make_buffered_reader(1)
        f.read(1)
        del f

    main()
    """)
    interp.run()
