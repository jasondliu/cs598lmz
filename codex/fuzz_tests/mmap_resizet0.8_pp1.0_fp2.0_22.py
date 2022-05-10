import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
That produces:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: cannot create mmap offset
</code>


A:

First, realize that <code>mmap</code> is a way to map arbitrary file/block devices into memory, and a memory-mapped file is just a special case of that.  As such, you have to be careful about your expectations regarding when a file's underlying bytes are synced to disk.  Unless you explicitly synchronize, it could be a long time before the filesystem knows about your changes.
Second, if you have a file descriptor <code>fd</code> for an open file, the following two calls are almost always equivalent:
<code>m = mmap.mmap(fd.fileno(), 0)
</code>
and
<code>m = mmap.mmap(fd, 0)
</code>
That is, Python will call <code>fd.fileno()</code> for you.  The exception is when <code>
