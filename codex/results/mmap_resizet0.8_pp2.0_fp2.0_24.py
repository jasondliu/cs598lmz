import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Result:
<code>Traceback (most recent call last):
  File "a.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: cannot read from mmap
</code>
I've read that this is normal and that I have to resize the memory-mapped region. But it's a problem since I don't know the length of the file before I try to mmap it, and it might change during the lifetime of the program.
I could try a file resize, catch the resulting exception (if the file shrinks) and then mmap the file again, but that still doesn't solve the problem: if the file shrinks, then it will fail.
So how should I do this?


A:

Instead of truncating the file, you can resize the mmap itself in-place:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

