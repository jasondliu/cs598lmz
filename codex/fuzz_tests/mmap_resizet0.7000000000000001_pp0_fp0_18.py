import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 6, in &lt;module&gt;
ValueError: mmap length is zero
</code>
I don't get this error if I don't read the mmap first.
Any ideas?


A:

<code>mmap.mmap()</code> is designed with the assumption that the file is not being written to by other processes at the same time. When you truncate the file, the length of the file changes, but the length of the mmap remains the same. This is the source of your error.

