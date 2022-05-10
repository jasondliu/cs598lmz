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
I'm using Python 3.5.2 on Windows 10.
How can I truncate the file without getting this error?


A:

You can't.
The mmap object is a view into the file.  If you truncate the file, the mmap object is no longer valid.  You have to close the mmap object before you truncate the file.

