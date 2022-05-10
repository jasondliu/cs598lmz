import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()
</code>
But I get an error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m[0] = b'2'
TypeError: 'mmap.mmap' object does not support item assignment
</code>
What am I doing wrong?


A:

You need to use <code>mmap.ACCESS_WRITE</code> to be able to write to the <code>mmap</code> object.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = b'2'
    m.close()
</code>

