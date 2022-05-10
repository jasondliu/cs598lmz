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

# test that the buffer is not deallocated
view[0] = 1

# test that the file object is deallocated
raise SystemError
""")

# issue #12166: test that the file object is not deallocated
# if the buffer is not deallocated
test.run_python_until_exit("""
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
view = None
del f

# test that the file object is deallocated
raise SystemError
""")

# test that the buffer is not deallocated
# if the file object is not deallocated
test.run_python_until_exit("""
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader
