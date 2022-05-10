import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line throws an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Is there a way to get a valid mmap object after truncating the file?


A:

You can't.
The <code>mmap</code> object is a view of the file, and the file is truncated.  The <code>mmap</code> object is still pointing to the old file.
You can create a new <code>mmap</code> object after truncating the file, but you can't use the old one.

