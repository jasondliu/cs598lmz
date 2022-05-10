import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This raises:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I would like to know if there is a way to prevent this error from happening.
I know that I can use <code>mmap.resize</code> to resize the mmap object, but I would like to know if there is a way to prevent the error from happening in the first place.


A:

The error is raised because the file size is 0, but the mmap offset is 1.
You can use <code>mmap.resize</code> to resize the mmap object, or you can use <code>mmap.remap</code> to remap the mmap object.

