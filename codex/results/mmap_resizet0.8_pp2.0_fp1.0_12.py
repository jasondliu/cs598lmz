import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Now, the <code>a</code> variable is b'\x01'. According to the docs, <code>m[:]</code> fetches all the contents of the file. I thought the file is empty at this point, but I guess I'm missing something.


A:

What you are missing is that the file is not empty when you access <code>m</code>, but it has been truncated to 0 at the time you call <code>a = m[:]</code> (i.e. <code>a</code> contains the data that was in the file before truncating it).
To get the results you expect (an empty bytestring) you could call <code>m.flush()</code> before truncating the file, or use <code>m[:] = b''</code> instead of <code>f.truncate()</code>.

