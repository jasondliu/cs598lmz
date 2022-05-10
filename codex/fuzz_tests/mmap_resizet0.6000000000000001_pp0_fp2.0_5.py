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
I guess the reason is that <code>m</code> keeps the file descriptor and doesn't notice that it was truncated.
Is there any way to update the mmap object (or create a new one) in such a way that it points to the beginning of the file?


A:

You could get around this by creating a new <code>mmap</code> object after truncating the file:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    f.seek(0)
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
</code>

