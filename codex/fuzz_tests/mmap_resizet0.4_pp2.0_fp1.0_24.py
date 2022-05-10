import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python35\lib\mmap.py", line 558, in __getitem__
    return self.read(len(item))
  File "C:\Users\user\AppData\Local\Programs\Python\Python35\lib\mmap.py", line 567, in read
    return self._read_bytes(size)
  File "C:\Users\user\AppData\Local\Programs\Python\Python35\lib\mmap.py", line 587, in _read_bytes
    return _mmap.mmap_read(self, size)
ValueError: read of closed file

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/user/Desktop/test.py", line 10, in &lt;module&gt;
    a = m[:]
  File "C:\Users\user\AppData
