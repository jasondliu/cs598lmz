import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0]
</code>
<blockquote>
<p>TypeError: an integer is required (got type str)</p>
</blockquote>
So you need to convert it back to a Python <code>int</code> before you can use it in Python.

