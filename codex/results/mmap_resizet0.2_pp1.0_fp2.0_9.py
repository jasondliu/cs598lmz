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
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening. I'm using Python 3.6.3 on Windows 10.


A:

<code>mmap</code> is a memory-mapped file. It's not a Python object, it's a system object. It's not a Python list, it's a memory-mapped file.
The <code>mmap</code> object is a view of the file. It's not a copy of the file. It's not a copy of the file's contents. It's a view of the file.
The <code>mmap</code> object is a view of the file. It's not a copy of the file. It's not a copy of the file's contents. It's a view of the file.
The <code>mmap</code> object is a view of the file.
