import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
But i got the <code>TypeError: 'str' does not support the buffer interface</code> error, how can I solve it?


A:

You can happily do this with Python 3:
<code>import mmap

with open('test.bin', 'wb') as f:
    f.write(bytes(1))

with open('test.bin', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes([2])
</code>
I changed the filename to make it easier to test.

