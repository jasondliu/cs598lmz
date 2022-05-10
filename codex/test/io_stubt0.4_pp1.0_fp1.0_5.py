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

# This should not crash.
view.tobytes()

# Issue #23602: test that the memoryview.tobytes() method
# works even if the underlying buffer is deallocated.

import io

class File(io.RawIOBase):
    def readinto(self, buf):
        self.buf = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
