import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line gives <code>ValueError: mmap offset is greater than file size</code>.
I'm not sure if this is a bug or not, but it seems like it should be possible to truncate a file and then mmap it, as long as the mmap offset is 0.
I'm using Python 3.4.3 on Windows.


A:

This is a bug in the Python implementation of <code>mmap</code>. The problem is that the <code>mmap</code> object caches the file size, and doesn't update it when the file is truncated.
The fix is to update the <code>mmap</code> object's cached file size when the file is truncated:
<code>def truncate(self):
    with self._lock:
        result = super().truncate()
        self._mmap.size = self.tell()
        return result
</code>
I've submitted a patch to the Python bug tracker.

