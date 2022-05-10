import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The error is:
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 6, in &lt;module&gt;
ValueError: mmap cannot extend file
</code>
This is because the file descriptor is still pointing to the end of the file.
In Python 2, the file descriptor is updated when you truncate the file.
Is there a way to do this in Python 3?

