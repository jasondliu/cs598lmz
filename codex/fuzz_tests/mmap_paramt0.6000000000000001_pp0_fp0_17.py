import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x00')
    m.seek(0)
    print(m.read(1))
</code>
It raises the following exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    print(m.read(1))
ValueError: mmap: can't find length of file
</code>
However, if I remove the <code>m.seek(0)</code> line, it works fine.
I'm using Python 3.4.3 on Windows 7.


A:

The problem is that the file is not being flushed to disk.  You need to call <code>flush</code> on the file object, or close it and re-open it before you call <code>mmap</code>.

