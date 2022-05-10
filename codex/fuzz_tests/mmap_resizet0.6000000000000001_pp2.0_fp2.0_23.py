import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    f.close()
</code>
Output:
<code>b'\x00'
</code>
This is a problem when I write to the file, and then close it, and then try to read it.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.write(bytes(2))
    f.close()
</code>
Output:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    f.write(bytes(2))
ValueError: I/O operation on closed file.
</code>
This is because the file is closed and the mmap still exists. I can't call the <code>m.close()</code> method because I don't want to call <code>close</code> on it manually, I want to use <code>
