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
view[0] = 1
""")
test.run_python_until_exit("""
""")
test.run_python_until_exit("""
class File(io.RawIOBase):
        global view
