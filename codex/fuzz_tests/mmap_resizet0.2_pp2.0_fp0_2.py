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
  File "test.py", line 8, in &lt;module&gt;
    a = m[:]
ValueError: mmap length is zero
</code>
I understand that the file is truncated, but I don't understand why the mmap is not updated.
I'm using Python 3.6.1 on Windows 10.


A:

The problem is that you are using <code>mmap.mmap</code> with the <code>length</code> parameter set to 0. This means that the mmap object is not actually mapped to any memory.
If you want to map the entire file, you should use <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)</code> instead.

