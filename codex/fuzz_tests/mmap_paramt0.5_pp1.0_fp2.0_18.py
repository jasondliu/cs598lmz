import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 50
</code>
<code>test</code> file contains <code>b'2'</code> after the execution of the code.

