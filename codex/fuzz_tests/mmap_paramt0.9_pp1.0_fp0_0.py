import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
m.move(0, 1, 2)
</code>
I get the error <code>OSError: [Errno 22] Invalid argument</code> on the <code>m.move()</code> step. What's going on? Is it a known bug?


A:

From the source of <code>mmap.py</code> (3.3):
<code>def move(self, dest, src, count):
    if not self.tagged:
        self._map_tagged()
    if not self.access:
        raise ValueError("mmap can't modify a mapped "
                         "aperture without MAP_SHARED")
    self.flush()  # before we change file position
    r = win32.MoveFileViewOfFile(self.map_handle,
                                 dest + self.offset,
                                 src + self.offset,
                                 count)
    if not r:
        raise OSError("MoveFileViewOfFile failed: " +
                      win32.FormatError())
</code>
I think that's an intended and documented
