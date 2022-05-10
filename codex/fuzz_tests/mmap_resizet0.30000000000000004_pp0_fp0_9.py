import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises an exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I guess it's because the file size is 0, but the mmap offset is 1.
Is there a way to make it work?


A:

You can't use the <code>mmap</code> object after truncating the file.
<code>mmap</code> is a view of a file, and when you truncate the file, the view is no longer valid.

