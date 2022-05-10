import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), length=1, access=mmap.ACCESS_WRITE, offset=0)
    direccion = m.find(b'\x01')
    m.close()

print(direccion)
</code>
This code is returning 0, but why not give me the position of the first byte of the file? The image show what is happening, the first byte is at the position 2.



A:

The offset you supply to <code>mmap</code> should be a multiple of <code>mmap.ALLOCATIONGRANULARITY</code>
EDIT:
Also you're looking for <code>bytes(1)</code>, but its actually <code>bytes([1])</code>

