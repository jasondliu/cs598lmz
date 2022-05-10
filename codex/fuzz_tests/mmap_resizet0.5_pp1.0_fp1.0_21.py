import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line fails with an <code>IndexError</code> exception:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
IndexError: mmap slice assignment is bigger than memory
</code>
Why is this?


A:

The <code>mmap</code> object is still holding a reference to the same memory region, but the file is now smaller, so the memory region is smaller.

