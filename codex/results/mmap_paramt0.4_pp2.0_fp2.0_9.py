import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
</code>
The last line gives me <code>TypeError: 'str' does not support the buffer interface</code>. 
Why does it happen? I thought that I'm writing to the file in binary mode.


A:

<code>bytes(1)</code> is a one-byte string, not a one-byte <code>bytes</code> object.
You need to use <code>bytes([1])</code> instead.

