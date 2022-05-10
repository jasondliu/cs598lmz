import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())

with open('test', 'rb') as f:
    print(f.read())
</code>
it prints
<code>b'\x02'
b'\x02'
</code>
But when I change the <code>mmap.mmap(f.fileno(), 0)</code> to <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> it prints
<code>b'\x02'
b'\x01'
</code>
Why does the <code>mmap.ACCESS_WRITE</code> flag revert the changes?


A:

<code>mmap.ACCESS_WRITE</code> is a constant that is defined as <code>mmap.PROT_WRITE | mmap.PROT_READ</code>.
<code>mmap.PROT_READ</code> is a constant that is defined as <code>0x1</code>.
