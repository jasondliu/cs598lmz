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
print(view)
</code>
This prints <code>None</code>, which I assume is the default value for <code>buf</code> in <code>readinto</code> in <code>io.RawIOBase</code>.
However, there are some comments in the <code>io</code> code that suggest that this value is in fact set to the view of the buffer passed to <code>readinto()</code>
<code>def readinto(self, b):
    """Read up to len(b) bytes into the writable buffer *b* and return
    the number of bytes read.  If the object is in non-blocking mode and
    no bytes are available, None is returned.

    .. versionchanged:: 3.3
       If the object is in non-blocking mode and no bytes are available,
       None is returned instead of raising ``BlockingIOError``.

    :raises BlockingIOError:
        if the object is in blocking mode and no data is available
    :raises TypeError:
        if the object is closed
    """
    self._checkClosed()
    if
