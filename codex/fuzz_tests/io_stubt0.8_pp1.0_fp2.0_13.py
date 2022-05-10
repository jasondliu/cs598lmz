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
del File
view # should raise AttributeError since `view` should have been deallocated
</code>
The above code is just for illustrative purposes; in my real code, the <code>File</code> object is used to read from a hardware device, and I need the read buffer to have a specific alignment, which is why I'm using <code>io.BufferedReader</code>.
I would expect the above code to raise <code>AttributeError</code>, since the underlying file object (<code>File</code>) should be deallocated and not hold reference to the buffer (<code>buf</code>), but that's not what happens. Is there something wrong in my code, or is this a bug in the standard library?
I'm using Python 3.5.3

