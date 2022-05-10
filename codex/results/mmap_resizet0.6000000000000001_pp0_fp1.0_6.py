import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)
</code>
The script works fine on Windows and Python 2.7, but fails on Linux with the following traceback:
<code>Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    a = m[:]
  File "/usr/lib/python3.4/mmap.py", line 101, in __getitem__
    return self.read(n)
  File "/usr/lib/python3.4/mmap.py", line 133, in read
    return self.obj.read(n)
ValueError: read of closed file
</code>
I'm aware that the <code>mmap</code> object must be closed before the underlying file is closed, but I don't see what could be wrong with my code.
