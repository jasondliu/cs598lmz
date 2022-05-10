import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(bytes(1))
    m.close()
</code>
The file <code>test</code> is now empty.
Is there a way to map a file without truncating it?


A:

The mmap file flags are based on the open file flags, so you need to open the file with <code>os.O_RDWR</code> instead of <code>os.O_WRONLY</code>.
<code>import os
import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    # pass os.O_RDWR instead of os.O_WRONLY
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(bytes(1))
    m.close()
</code>

