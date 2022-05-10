import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 49 # 1

with open('test', 'rb') as f:
    print(f.read()) # b'1'
</code>
The original answer:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes([49]) # 1

with open('test', 'rb') as f:
    print(f.read()) # b'1'
</code>

