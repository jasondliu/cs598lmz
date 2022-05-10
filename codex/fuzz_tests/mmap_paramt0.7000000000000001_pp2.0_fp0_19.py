import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(bytes(2))
    m.close()

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    print(m.read(1))
    m.close()
</code>
Output is <code>b'\x02'</code> (which is the expected value).
If you attempt to open the file with <code>os.open</code> and then pass the file descriptor to <code>mmap.mmap</code> (which is what I think you're doing), you need to make sure that <code>os.open</code> is called with the <code>os.O_RDWR</code> flag:
<code>import os
import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', os.O_RDWR) as f:
    m = mmap.mmap(f.fileno(), 0)
    m.
