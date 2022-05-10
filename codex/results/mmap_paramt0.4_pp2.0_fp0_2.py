import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
</code>
But it fails with:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.resize(10)
ValueError: mmap length is zero
</code>
I've tried different combinations of <code>mmap.MAP_SHARED</code> and <code>mmap.MAP_PRIVATE</code> but nothing seems to work.
How can I resize the file using <code>mmap</code>?


A:

You need to specify the length of the file when you create the <code>mmap</code> object:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.resize(10)
</code>

