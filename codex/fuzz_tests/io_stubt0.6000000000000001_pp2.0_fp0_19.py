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
view[0] = b'x'
</code>
What should happen here?  Is this safe?  Should we even attempt to support this?  Or should the reference count drop to zero immediately, and we should just treat this as a memory error?
I'm guessing we should attempt to support it, since that seems to be the intent of the <code>RawIOBase</code> interface.  But it's not clear to me that that's a good idea.

The second issue is how to implement <code>io.BufferedReader.readinto</code> and <code>io.BufferedReader.readinto1</code>.
The idea is that we should be able to pass in a very large buffer, and we should fill it from the buffer and the underlying file until either we run out of data, or the buffer is full.  The difference between <code>readinto</code> and <code>readinto1</code> is that <code>readinto1</code> should return at least one byte, or return zero bytes if the buffer is empty.  (This is the same as <code>read1</code> and <code>read</
