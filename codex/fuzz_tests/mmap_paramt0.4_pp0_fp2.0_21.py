import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
This code works on Ubuntu 16.04, but it raises <code>TypeError: a bytes-like object is required, not 'int'</code> on Windows 10.
I found that <code>bytes(1)</code> returns <code>b'\x01'</code> on Ubuntu, but <code>1</code> on Windows.
How can I write <code>bytes(1)</code> to a file on Windows?


A:

<code>bytes(1)</code> returns a single byte (of value 1) on both platforms. The difference is that <code>bytes(1)</code> returns an object of type <code>bytes</code> on Python 3, but <code>str</code> on Python 2.
The error message is misleading, but the problem is that you are trying to write a single byte to the file. You need to write a byte string, a sequence of bytes.
<code>with open('test', 'wb') as f:
    f.write(bytes([1]))
</code>

