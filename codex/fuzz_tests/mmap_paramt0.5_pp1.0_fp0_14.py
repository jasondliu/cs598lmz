import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = bytes(2)
</code>
I expected the result to be a file containing the byte 2, but the result is a file containing the byte 1. If I close the file, then open it again and read it, the result is the byte 2. How do I get the file to be written immediately?


A:

You need to use <code>mmap.flush</code> to ensure that changes are written to disk:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = bytes(2)
    m.flush()
</code>

