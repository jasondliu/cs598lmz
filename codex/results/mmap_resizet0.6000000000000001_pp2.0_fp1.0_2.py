import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The problem is, the <code>a = m[:]</code> line throws an exception.
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
What I don't understand is why the <code>f.truncate()</code> line doesn't update the mmap object.
I could get around the problem by first getting the size of the mmap object and then truncating the file to that size, but that feels like a hack.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m_size = m.size()
    m.close()
    f.truncate()
    m = mmap.mmap(f.fileno(), m_size)
    a = m[:]
</code>
Is there a better way?


A:

<code>mmap</code> is just
