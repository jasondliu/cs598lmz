import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "C:\Users\user\AppData\Local\Programs\Python\Python35\lib\mmap.py", line 1215, in __getitem__
    data = self.read(len(result))
  File "C:\Users\user\AppData\Local\Programs\Python\Python35\lib\mmap.py", line 556, in read
    return self._read_bytes(size)
  File "C:\Users\user\AppData\Local\Programs\Python\Python35\lib\mmap.py", line 586, in _read_bytes
    raise error(ENOENT, "mmap can't read file")
OSError: [Errno 22] mmap can't read file

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/user/Desktop/pytest.py", line 8, in &lt;module&gt;

