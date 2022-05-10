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

# This used to fail because the underlying object was not kept alive
# during the readinto call.  This also tests that the underlying object
# is closed when the buffer is deleted.
buf[0]
"""

def test_main():
    test.support.run_unittest(BufferedReaderTest)

if __name__ == "__main__":
    test_main()
