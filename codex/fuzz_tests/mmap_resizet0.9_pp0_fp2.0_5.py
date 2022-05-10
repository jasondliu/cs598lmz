import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
In the above code we create test file with 1 byte and truncate it to zero bytes. Reading the memory mapped area gives empty bytes.
But if I applied the same code with disk backed buffer I am getting unexpected results.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ALLOCATIONGRANULARITY, offset=0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This time I am getting <code>mmap.error: [Errno 22] Invalid argument</code> at the line <code>a = m[:]</code>. If I print <code>m.read(1)</code> it gives <code>b'\x00'</code>. So in this case the file is truncated to zero bytes but mmap reading gives that byte.
Why is it giving that byte? And how to read the
