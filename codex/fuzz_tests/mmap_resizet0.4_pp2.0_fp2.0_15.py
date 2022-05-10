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
  File "C:\Users\user\Desktop\test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
How can I prevent this error?


A:

The <code>mmap</code> object is not aware that the underlying file has been truncated. The underlying file is truncated, but the <code>mmap</code> object still thinks that the file is 1 byte long.
You could use <code>m.resize(0)</code> to make the <code>mmap</code> object aware of the truncation.

