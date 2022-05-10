import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)

with open('test', 'r+b') as f:
    print(f.read(2))
</code>
Output:
<code>b'\x01\x00'
</code>
When creating an mmap via 'create' or 'readwrite' methods <code>protect</code> has to be set to <code>mmap.ACCESS_WRITE</code> or I'm getting <code>ValueError: cannot resize readonly memory map</code>.
Is there any way to resize a shared memory mapping without an explicit permission to write?

