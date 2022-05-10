import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    # m[1] = bytes(1) # segfault
    # m[0] = bytes(1) # works
</code>
To me, m[0] shouldn't work because I didn't write anything there and the size of the file is 1 byte. Am I missing something?
It's a problem because mmap(2) suggests mapping the whole underlying file on Linux, however it is not possible to extend the file via <code>truncate</code>, the only way would be to to map the whole file and write zeros everywhere (even though I expect the kernel to do that for me on page fault).
<code>import mmap
import os

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    os.truncate(f.fileno(), 0x10000)
    print(os.stat('test').st_size) # 0x10000
    m = mmap.mmap(f.fileno(), 0x10000)
    print(m.find(bytes(1))) #
