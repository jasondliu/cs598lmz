import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I'm not sure why this is happening. I thought that the <code>mmap</code> object would be updated when the file is truncated. Is there a way to get around this?


A:

The problem is that the <code>mmap</code> object is not updated when the file is truncated.
The solution is to use <code>mmap.resize</code> to resize the <code>mmap</code> object.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(f.tell())
    a = m[:]
