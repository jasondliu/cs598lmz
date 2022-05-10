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
print(view.tobytes())
</code>
The buffer is filled with b'a' (raw bytes) as expected. Close the buffer and check its contents. Now, create a new buffered reader. Its buffer has a different memory address from the one we just used. We have to fill it in the same way again, which we can do so without doing anything (we didn't delete b then either), and we can read how many bytes we want. In fact, we can always just fill it.
Now, this is not a trivial problem, but I think it is possible to solve.

