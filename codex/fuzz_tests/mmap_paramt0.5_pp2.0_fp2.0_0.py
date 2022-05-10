import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x00')
</code>
The last line throws:
<code>Traceback (most recent call last):
  File "/usr/lib/python3.5/mmap.py", line 276, in write
    return self.move(offset, len(s), 0, s)
  File "/usr/lib/python3.5/mmap.py", line 247, in move
    self._check_size(offset, size)
  File "/usr/lib/python3.5/mmap.py", line 242, in _check_size
    raise ValueError('mmap offset is greater than file size')
ValueError: mmap offset is greater than file size
</code>
But if I change the last line to:
<code>m.write(bytes(1))
</code>
It works.
What's going on here?


A:

You are using the wrong <code>write()</code> function; you are calling <code>mmap.mmap.write()</code> instead of <code>file.write()</code>:
