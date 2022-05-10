import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = '2'
    m.flush()
</code>
But it doesn't work. I get the following error:
<code>Traceback (most recent call last):
  File "./test.py", line 10, in &lt;module&gt;
    m[0] = '2'
TypeError: 'str' does not support the buffer interface
</code>
I'm using Python 3.2.3 on Ubuntu 12.04.
Any idea?


A:

Use <code>m[0] = b'2'</code> to write a single byte with value <code>2</code>.

