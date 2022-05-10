import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>a</code> is <code>b''</code>, but I would expect it to be <code>b'\x01'</code>.
This is the case for Python 2.7 and Python 3.4.


A:

<code>mmap</code> does not know about the file being truncated.  In fact, the <code>mmap</code> call does not even know about the file being opened.  It just gets a file descriptor and uses that.  So, <code>mmap</code> sees the file as having the same size as before, even though the file handle you used to create the <code>mmap</code> object has been truncated.

