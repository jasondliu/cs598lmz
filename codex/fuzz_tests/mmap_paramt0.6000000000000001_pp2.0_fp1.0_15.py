import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = bytes(0)
    m.flush()
</code>
I get the following error:
<blockquote>
<p>TypeError: an integer is required (got type bytes)</p>
</blockquote>
I'm using Python 3.4.2 on Windows 8.1.


A:

<code>bytes</code> is a Python 3 type, not a Python 2 type.
In Python 2, you should use <code>str</code> instead, or <code>bytearray</code>, which is a mutable <code>str</code>.

