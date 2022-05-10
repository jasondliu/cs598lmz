import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I don't understand why this error occurs.
I've tried to use <code>m.resize(0)</code> and <code>m.close()</code> instead of <code>f.truncate()</code> but it doesn't work.


A:

You are trying to access a memory mapped file that is no longer valid.
The <code>mmap</code> object is a wrapper around a memory mapped file, which is a file that is mapped into memory. The <code>mmap</code> object is just a Python object that provides a view into that memory.
When you truncate the file, you are removing the file from the filesystem. The memory mapped file is no longer valid.
You can't access the memory mapped file after you truncated the file.

