import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: memory mapping has been closed
</code>
What am I doing wrong?


A:

It's not clear from the docs, but the <code>mmap</code> object is actually tied to the size of the underlying file (at least on Linux).  If you truncate the file, the <code>mmap</code> object is no longer valid.  In particular, if you try to read from it (as you do in your <code>a = m[:]</code> line), you get a <code>ValueError</code>.
If you want to keep the <code>mmap</code> object open, you will have to write some data to the file to restore the original size.

