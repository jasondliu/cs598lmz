import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I was expecting to segfault, but I'm getting an IOError instead. And there doesn't seem to be a segfault here.
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
IOError: [Errno 5] Input/output error
</code>
Is this behavior well-defined? Is there a way to segfault here (short of deliberately corrupting memory outside the memory mapped region)?


A:

mmap is for mapping files (or other things) onto memory, <code>open</code> does not created mmapped files as a matter of course.

