import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(m)
    m[:] = b'\0'
    print(m)
</code>
output:
<code>&lt;mmap.mmap object at 0x7f1278c00570&gt;
&lt;mmap.mmap object at 0x7f1278c00570&gt;
</code>
https://docs.python.org/3/library/mmap.html

