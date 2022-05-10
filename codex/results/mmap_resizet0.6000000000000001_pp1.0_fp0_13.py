import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The first mmap.mmap call fails with:
<code>Traceback (most recent call last):
  File "./test.py", line 9, in &lt;module&gt;
    m = mmap.mmap(f.fileno(), 0)
ValueError: mmap length is zero
</code>
Why does removing the first mmap.mmap call make the second work?


A:

I think the problem is that you're mapping the file before you truncate it, so the length is already zero.

