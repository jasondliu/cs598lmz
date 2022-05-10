import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'0'
</code>
I have got the following error:
<code>Traceback (most recent call last):
  File "test_mmap.py", line 8, in &lt;module&gt;
    m[0] = b'0'
ValueError: cannot modify size of mapped region
</code>
I guess it's because I have to set the size of memory-map when initializing the <code>mmap</code> object. However, I have no idea how to do so.


A:

The mmap size should be the same as the size of the file.
If you want to expand the file, you need to use <code>resize</code> method.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[0] = b'0'
    m.resize(2)
    m[1] = b'
