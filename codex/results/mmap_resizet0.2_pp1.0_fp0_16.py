import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I expected <code>a</code> to be <code>b''</code>.
I'm using Python 3.5.2 on Ubuntu 16.04.


A:

The problem is that the <code>mmap</code> object is still pointing to the old file size.  You can fix this by calling <code>m.resize(0)</code> after truncating the file.

