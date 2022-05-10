import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This gives me the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap closed or invalid
</code>
I would expect the mmap to be invalidated, but not closed. I would expect the following to work:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
    print(a)
</code>
But it doesn't. Why is this?


A:

The <code>mmap</code> object is closed because the file is truncated.
The <code>mmap</code> object is a wrapper around a memory-mapped file. When you truncate the file, the memory-mapped file is
