import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.write(bytes(2))
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.resize(2)
ValueError: resize() cannot extend the file
</code>
I'm using Python 3.5.2 on Ubuntu 16.04.


A:

The <code>mmap</code> module is not designed to extend the file. It is designed to map a file into memory.
If you want to extend the file, you can use the <code>os</code> module:
<code>import os

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    os.ftruncate(f.fileno(), 2)
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>

