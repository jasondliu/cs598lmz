import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(16)
    print(m.find(b'\x00'))
</code>
The above code produces <code>1</code>, indicating that the first <code>\x00</code> is found at the 1st byte after the original single byte.
But when I try the same code on a file in Windows with the file handle:
<code>with open('test', 'r+b', buffering=0) as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(16)
    print(m.find(b'\x00'))
</code>
It fails with:
<code>Traceback (most recent call last):
  File "test.py", line 6, in &lt;module&gt;
    print(m.find(b'\x00'))
TypeError: a bytes-like object is required, not 'int'
</code>
Apparently <code>m</code> is an integer now, but why?

