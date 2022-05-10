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
  File "mmap_test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot read from closed file
</code>
How can I make the mmap object aware of the file size change?


A:

You can't.  The mmap object is a view of the file, and the file has been truncated.  You need to close the file and mmap object, then reopen them.  It's a bit of a pain, but it's the way it is.

