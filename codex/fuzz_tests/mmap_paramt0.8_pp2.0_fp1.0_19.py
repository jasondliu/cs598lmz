import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = b'\x00'
</code>
<blockquote>
<p>TypeError: must be bytes-like object, not 'str'</p>
</blockquote>
Is it possible to write a null byte to a file without using the write method?


A:

The null byte is just a single byte, so you can write it like this:
<code>m[0:1] = b'\x00'
</code>

