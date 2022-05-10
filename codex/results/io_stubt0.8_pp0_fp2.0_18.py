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

# This is a bug. The buffer of the underlying File() object is destroyed
# when the BufferedReader() is deleted. But it is still used through the
# bytearray in buf. This is a violation of the memoryview requirements.
buf = view.tobytes()
