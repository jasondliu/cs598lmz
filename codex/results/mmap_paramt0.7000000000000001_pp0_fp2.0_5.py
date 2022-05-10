import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(256 * 256 * 256)
</code>
When I run this code I get <code>mmap.error: [Errno 22] Invalid argument</code>. I know that this error is caused by the <code>resize</code> call, but I don't understand why it occurs. What am I missing here?
P.S. I am using Python 3.6.1 on Ubuntu 16.04.


A:

The resize function is not supported on all systems. For example, on Linux with Python 3.4.3, the following code works:
<code>import mmap

with open('test', 'wb') as f:
    f.write(b'\x00')

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(256 * 256 * 256)
</code>
but if I use Python 3.5.2, or Python 3.6.1, I get the same error as you. 
The Python 3.5.2 docs say that resize
