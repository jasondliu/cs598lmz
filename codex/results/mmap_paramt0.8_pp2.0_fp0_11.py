import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
    m[0] = 0x01

with open('test', 'rb') as f:
    print(f.read(1))
</code>
which prints <code>b'\x01'</code> as expected.
However, a file created with <code>touch test</code> is not writable using this method (the <code>mmap</code> call raises <code>PermissionError</code>). What is the difference here?

