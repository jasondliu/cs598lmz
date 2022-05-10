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
output
<code>b'\x00'
Traceback (most recent call last):
  File "D:/test.py", line 10, in &lt;module&gt;
    a = m[:]
  File "D:\python\lib\mmap.py", line 257, in __getitem__
    s = self.read(offset + len(s))
  File "D:\python\lib\mmap.py", line 379, in read
    if self.closed:
ValueError: I/O operation on closed file.
</code>


A:

One possible cause is when you assigned <code>a = m[:]</code> the file itself was exclusive opened the <code>m</code> object, causing <code>f.truncate()</code> to raise a <code>ValueError</code>. You can avoid this by setting <code>access</code> parameter of <code>mmap.mmap</code> to <code>mmap.ACCESS_READ</code>.
From <code>mm
