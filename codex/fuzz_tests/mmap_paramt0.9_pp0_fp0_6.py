import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ|mmap.PROT_WRITE)
    print(m.seek(0))
    print(m.write(bytes(3)))
    print(m.read(1))
    print(m.seek(0))
    print(m.read(1))
</code>
Output:
<code>0
3
b''
0
b'1'
</code>
The value that was originally written is still at <code>index 0</code>, even though I seeked past it. When I tried to write the value <code>3</code>, it instead wrote it to the end of the file and then didn't move the pointer. So when I read bytes, it still read the start of the file.
The answer is to use:
<code>f.seek(0, os.SEEK_SET)</code>
So the working code is:
<code>import mmap
import os

with open('test', 'wb') as f:
    print(f.write(bytes(1)))

with open('test', 'r+b') as f
