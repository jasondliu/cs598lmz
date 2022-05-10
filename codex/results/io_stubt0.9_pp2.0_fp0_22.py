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
%timeit io.BufferedReader(File()).read(1)
%timeit io.BufferedReader(File()).read(2)
%timeit io.BufferedReader(File()).read(4)
%timeit io.BufferedReader(File()).read(8)
%timeit io.BufferedReader(File()).read(16)
%timeit io.BufferedReader(File()).read(32)
%timeit io.BufferedReader(File()).read(64)
%timeit io.BufferedReader(File()).read(128)
%timeit io.BufferedReader(File()).read(256)
%timeit io.BufferedReader(File()).read(512)
%timeit io.BufferedReader(File()).read(1024)
%timeit io.BufferedReader(File()).read(2048)
%timeit io.BufferedReader(File()).read(4096)
%timeit io.BufferedReader(File()).read(8192)
%timeit io.BufferedReader(File()
