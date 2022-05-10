import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.read(1)
    m.write_byte(b'\x00')
    m.read(1)
</code>

But at the same time I cannot update the first byte of the file like so:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write_byte(b'\x00')
    m.read(1)
</code>
The error I get is:
<code>mmap.error: [Errno 22] Invalid argument
</code>


A:

You cannot randomly overwrite bytes in a file, there is nothing that can even make sense of it. Yes, if a file is created with a given length, and that length is determined by the first available block, there can be a first byte, but it is meaningless. Everything the OS will care about is what the current size is, which is determined by the number of allocated blocks.

