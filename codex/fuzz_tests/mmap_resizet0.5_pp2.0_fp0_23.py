import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is wrong size
</code>
I thought that perhaps <code>mmap.mmap</code> would have a <code>resize</code> method, but it doesn't.
Is there a way to resize a mmap object?
I am using Python 3.4.3


A:

<code>mmap</code> is a wrapper for the <code>mmap()</code> system call. The <code>mmap()</code> system call doesn't allow you to resize a memory-mapped file. You have to <code>close()</code> the <code>mmap</code> object and then create a new one with the new size.

