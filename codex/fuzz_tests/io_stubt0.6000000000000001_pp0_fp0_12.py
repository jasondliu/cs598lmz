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
</code>
I was hoping to have <code>view</code> point to the data in the buffer, but this is not the case.  The <code>view</code> is an array with a copy of the data.  This makes sense, since the buffer is re-used and the data can be modified before <code>f</code> is deleted. 
So, my question is: Is there a way to have a view on the buffer data?  I know I can use <code>f.raw.readinto(view)</code>, but it seems so unnecessary.

