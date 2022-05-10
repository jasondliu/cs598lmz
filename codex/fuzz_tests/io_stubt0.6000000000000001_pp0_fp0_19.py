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
</code>
The problem is that <code>buf</code> (which is <code>view</code> in this example) does not get freed when <code>f</code> is deleted. It is possible to force the garbage collector to free it by doing <code>gc.collect()</code>, but this is not a good practice.
Also, <code>view</code> is not freed when <code>f</code> is deleted (i.e. <code>f.close()</code> is called) because, according to the documentation, <code>close()</code> doesn't do anything.
The documentation of <code>io.RawIOBase.readinto()</code> says:
<blockquote>
<p>The buffer must be writable. It will be written to <strong>starting at offset 0</strong> and extending for <strong>exactly n bytes</strong>; no additional bytes will ever be written. The total number of bytes read into the buffer should be returned; if only some bytes could be read, return whatever the io object was able to read. <strong>If 0 bytes are returned, and
