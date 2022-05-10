import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The result is:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
  File "/usr/lib/python3.5/mmap.py", line 322, in __getitem__
    self._check_find(self.find(sub, start, end))
  File "/usr/lib/python3.5/mmap.py", line 335, in _check_find
    raise ValueError("mmap closed or invalid")
ValueError: mmap closed or invalid
</code>
It seems that mmap is not aware of file changes. Is it possible to make mmap aware of it?
I am using python 3.5.2 on Ubuntu 16.04.


A:

<code>mmap</code>s are only guaranteed to be consistent with the underlying file at the time of creation. If you want to update the file and then read the updated version, you need to create a new <code>mmap</code>.

