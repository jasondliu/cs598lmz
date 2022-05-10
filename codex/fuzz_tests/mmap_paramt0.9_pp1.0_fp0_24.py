import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    
with open('test', 'rb') as f:
    print(f.read())

</code>
this gives <code>b'\x02'</code> as expected. See also documentation for <code>mmap.mmap</code>.

