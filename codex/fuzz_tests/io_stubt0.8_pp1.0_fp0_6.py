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
print view
try:
    view.zero()
except:
    pass
print view
print [0 for x in view]
EOF
./python -c 'import sys; exec(sys.stdin.read())'
""")

    def test_bytearray_rw_memoryview(self):
        # Issue #8018
        self.assertEqual(self.run_python(r"""print type(memoryview(bytearray(b"abc")))"""), '<type \'memoryview\'>')

    def test_array_tobytes(self):
        self.assertEqual(self.run_python(r"""print type(array.array('i',[1,2,3]).tobytes())"""), '<type \'str\'>')

    def test_array_frombytes(self):
        self.assertEqual(self.run_python(r"""
import array
a=array.array('i')
a.frombytes(b"ab")"""), 'Traceback (most recent call last):\n  File "<string>", line 2, in
