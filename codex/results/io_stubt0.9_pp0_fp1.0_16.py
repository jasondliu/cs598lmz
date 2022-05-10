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
</code>
(This works in Python 2.7; I don't have access to Python 3.x.)


A:

Normally, I wouldn't use <code>gc</code> as CPython has a very fast builtin reference counting system. However, in this case it can be used with some caveats:
First, <code>gc.garbage</code> is not public API, <code>collect</code> is the public interface.
Second, you should be sure you know what object you want to gc first before collecting because the collector will collect any unreachable objects at the time it runs, not just the one that you want to collect. If you want to force collection of just one object, you should use a weakref on it and later do a <code>collect</code> so that object is the only object that is collected and available in <code>gc.garbage</code>.
Lastly, the point of the last warning is that if you using the streaming API, at the point you do a <code>collect</code>, the file object has been closed and it closes the stream and so there is no way at that point, that you would see
