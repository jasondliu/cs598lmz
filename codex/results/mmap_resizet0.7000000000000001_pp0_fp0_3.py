import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print('a is', a)
</code>
This produces the following output:
<code> a is b''
</code>
The way I understand this is that the file is opened and the mmap is created from the file descriptor. The file is truncated, then the mmap is read. Since the file is empty, the mmap should be empty. However, the mmap contains the non-empty byte string. Is this correct?

