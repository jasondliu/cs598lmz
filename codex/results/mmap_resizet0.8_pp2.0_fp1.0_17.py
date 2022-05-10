import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get an error message:
<code>Traceback (most recent call last):
  File "C:/Python/temp/mmap-delete-overflow.py", line 13, in &lt;module&gt;
    a = m[:]
  File "C:\Python\lib\mmap.py", line 148, in __getitem__
    data = self.read(size)
  File "C:\Python\lib\mmap.py", line 276, in read
    return self._mmap.read(size)
ValueError: read of closed file
</code>
or, if I replace <code>f.truncate()</code> with <code>m.resize(0)</code>, the error is:
<code>Traceback (most recent call last):
  File "C:/Python/temp/mmap-delete-overflow.py", line 13, in &lt;module&gt;
    a = m[:]
  File "C:\Python\lib\mmap.py", line 140, in __getitem__
   
