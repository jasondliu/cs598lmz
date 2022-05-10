import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I would expect <code>a</code> to be <code>b''</code>.
I'm using Python 3.6.5 on Windows 10.


A:

The <code>mmap</code> object is not updated when the file is truncated.
You can use <code>m.resize(0)</code> to update the <code>mmap</code> object.

