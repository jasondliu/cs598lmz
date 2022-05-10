import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following exception:
<code>Traceback (most recent call last):
  File "mmap_test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot resize memory map
</code>
Is there any way to resize the mmap object after the underlying file has been truncated?


A:

The <code>resize()</code> method is apparently not available on all platforms.  It's not available on Windows, for example.  If you need to resize the memory map, you can unmap it first and then map it again with a new size:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    m = mmap.mmap(f.fileno(), 0)
</code>

