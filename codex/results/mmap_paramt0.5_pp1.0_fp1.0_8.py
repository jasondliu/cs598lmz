import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x00')
</code>
This will create a new file <code>test</code> with a single byte of value <code>1</code>. It will then open the file and map it into memory, and overwrite the byte with a <code>0</code>.

