import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())
</code>
But this throws the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m.write(bytes(2))
TypeError: write() argument must be a string, not int
</code>
I am running Python 3.5.2 on Ubuntu 16.04.
What is going wrong here?
I've tried various combinations of <code>mmap.ACCESS_READ, mmap.ACCESS_WRITE, mmap.ACCESS_COPY</code> and <code>mmap.MAP_SHARED, mmap.MAP_PRIVATE</code> but I haven't found any that work.


A:

You're using <code>bytes</code> incorrectly.
<code>bytes(2)</code> is not a <code>bytes</code> object containing the value <code>2</code>.  It is a <code>bytes</code> object
