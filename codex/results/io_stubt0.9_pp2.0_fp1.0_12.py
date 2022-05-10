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
view

# XXX issues:
# - we get a segfault when using "f = io.BufferedReader(File())". 
# - we get ValueError: invalid readbuffer size when reading from the file descriptor.
# - we get a ValueError: underlying buffer is not writable when using io.RawIOBase without io.BufferedReader.
