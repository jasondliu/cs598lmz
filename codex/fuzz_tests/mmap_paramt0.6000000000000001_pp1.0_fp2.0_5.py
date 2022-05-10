import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x01'
</code>
The problem is that I need the file to be opened in read-only mode, but when I do <code>open('test', 'rb')</code> I get the following error:
<code>mmap.mmap(f.fileno(), 0)
mmap.error: [Errno 12] Cannot allocate memory
</code>
I am using python 3.5.2 on windows 10.

