import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('a')
    m.close()
</code>
This works in Python 2.7.6, but not in 3.4.2.  In 3.4.2, I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 9, in &lt;module&gt;
    m[0] = ord('a')
TypeError: 'mmap' object does not support item assignment
</code>
I can't find any documentation that <code>mmap</code> objects are immutable in Python 3.  Is this a bug in Python 3?


A:

According to the 3.4 documentation, <code>mmap</code> objects are read-only by default.  You need to pass <code>access=mmap.ACCESS_WRITE</code> to the <code>mmap</code> constructor to get a writable <code>mmap</code> object.

