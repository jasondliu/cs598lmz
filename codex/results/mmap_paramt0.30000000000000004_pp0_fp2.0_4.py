import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(0))
    m.close()
</code>
I get
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m.write(bytes(0))
ValueError: mmap can't modify a readonly or copy-on-write memory map
</code>
I don't understand why. I am opening the file in read/write mode. What am I missing?


A:

The <code>mmap</code> object is not a file object, and it doesn't inherit the file's mode.  You need to specify the mode when you create the <code>mmap</code> object.
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
</code>

