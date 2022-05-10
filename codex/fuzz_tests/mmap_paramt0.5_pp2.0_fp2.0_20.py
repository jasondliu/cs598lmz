import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m[0] = 255
    m[0] = 256
</code>
I get the following error:
<code>ValueError: byte must be in range(0, 256)
</code>
This seems to be a bug in mmap, since <code>bytes</code> accepts 256, and <code>bytes([256])</code> returns <code>b'\x00'</code>.


A:

The <code>mmap</code> module is a wrapper around the C <code>mmap</code> function, which has the following signature:
<code>void *mmap(void *addr, size_t len, int prot, int flags, int fildes, off_t off);
</code>
The <code>mmap</code> function is a low-level interface to memory mapping, and it is not concerned with the interpretation of the bytes in the mapped region.  It's up to the user to make sure that the bytes are interpreted correctly.  For example, the C <code>memcpy</code> function has the following signature:

