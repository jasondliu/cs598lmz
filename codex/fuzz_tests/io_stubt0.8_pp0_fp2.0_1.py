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
""")

def test_file_readinto_2(space):
    w_ret = space.appexec([], """():
        import io
        buf = b'test'
        with open(__file__, 'rb') as f:
            n = f.readinto(buf)
            return n, buf
    """)
    assert space.unwrap(w_ret) == (4, b'test')


def test_buffered_io_write_readinto_1(space):
    skip("skip this test for now")
    w_ret = space.appexec([], """():
        import io
        f = io.BufferedWriter(io.BytesIO())
        f.write(b'abc')
        f.flush()
        f.seek(0)
        f.readinto(bytearray(3))
        return f.tell()
    """)
    assert space.int_w(w_ret) == 3


def test_buffered_io_write_readinto_2(space):
    skip("skip this test for now
