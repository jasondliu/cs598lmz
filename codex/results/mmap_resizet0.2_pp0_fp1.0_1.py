import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I don't understand why this happens. I thought that the mmap object would be updated when the file is truncated.
Is there a way to make this work?


A:

You can't truncate a file that is mmap'd.  The mmap object is a view into the file, and if you truncate the file, the mmap object will be invalid.

