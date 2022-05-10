import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I am getting the error:
<code>Traceback (most recent call last):
  File "test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I am trying to simulate a situation when the file is truncated by another process. Is there a way to make this work?


A:

When you truncate the file, you are also truncating the mmap.  You need to create a new mmap for the file after truncating it.

