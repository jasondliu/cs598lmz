import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'b'
    m.close()

with open('test', 'r') as f:
    print(f.read())
</code>
When I run this, I get this error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    m[0] = b'b'
TypeError: must be read-write bytes-like object, not memoryview
</code>
I'm a bit confused about this error.  I thought that <code>m</code> is a read/write bytes-like object, since I opened the file with <code>r+b</code>.  What am I doing wrong?

I'm running python 3.6.1 on Mac OS X 10.11.6


A:

<code>mmap</code> objects do not support item assignment. Use <code>m[:] = b'b'</code> or <code>m.write(b'b')</code> instead.

