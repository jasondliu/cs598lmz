import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Вывод:
<code>Traceback (most recent call last):
  File "/usr/lib/python3.7/mmap.py", line 1251, in __getitem__
    buf = self.read(size)
  File "/usr/lib/python3.7/mmap.py", line 1149, in read
    n = n + self._toread
ValueError: positive overflow in readsize

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
  File "/usr/lib/python3.7/mmap.py", line 1264, in __getitem__
    return mmap_as_buffer(self)[key]
  File "/usr/lib/python3.7/mmap.py", line 1190, in __getitem__
    data = self._read(size, offset)
  File "/usr/lib/python3.7/mmap.py", line 11
