import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())
</code>
This prints <code>b'\x02'</code> as expected.
However, if I try to do the same thing with a memory-mapped file, the file is not updated:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())
</code>
This prints <code>b'\x01'</code>.
I have tried to call <code>m.flush()</code> after <code>m.write(bytes(2))</code>, but that doesn't help.
How can I update the file using the memory-mapped file?


A:

The <code>mm
