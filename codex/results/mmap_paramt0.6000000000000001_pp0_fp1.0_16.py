import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
The above code throws <code>TypeError: 'str' does not support the buffer interface</code>
However, the following code works:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
</code>
Why is that?


A:

The error message says it all: <code>str</code> does not support the buffer interface, but <code>int</code> does.

