import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    del m
    a = m[:]
    print(a)
</code>
output
<code>b'\x01'
Traceback (most recent call last):
  File "test.py", line 12, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
How do I get <code>mmap</code> to re-read the file size?  Or is there a better way to do this?


A:

You can't. If you check the <code>m.size()</code>, it will return <code>0</code>.
You need to close the <code>mmap</code> object and create a new one.

