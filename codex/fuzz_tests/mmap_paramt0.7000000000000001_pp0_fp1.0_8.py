import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
And it works fine. But if I try to write <code>bytes(1, byteorder='little')</code> it gives me <code>TypeError: 'str' does not support the buffer interface</code>.
Is there a way to make it work with little endian?

