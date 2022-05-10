import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(bytes(b'\x00'))

# Access a single byte
with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    byte = m.read_byte()
    print(byte)
    # 0

# Access two bytes at once
with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    bytes = m.read(2)
    print(bytes)
    # b'\x00\x00'
</code>

