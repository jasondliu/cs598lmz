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
This code successfully sets <code>view</code> to a memoryview which describes the buffer of the <code>BufferedReader</code> instance. However, the size of this buffer is 8192, which is the default size of a <code>BufferedReader</code> object.
I would like to change this size, but I cannot find a way to do so. The constructor does not accept any arguments other than the file-like object to wrap. The <code>BufferedReader</code> class does not seem to have any methods to change the size of the buffer. There is a <code>BufferedRandom</code> class, which does have a <code>raw</code> attribute, but it is not a <code>memoryview</code>.
I am using Python 3.4.3 and I cannot upgrade to a newer version of Python.
How can I change the size of this buffer?


A:

I think you're out of luck.  <code>BufferedReader</code> is a <code>_BufferedIOBase</code>, which is an abstract base class.  It's not meant to be instantiated directly.
