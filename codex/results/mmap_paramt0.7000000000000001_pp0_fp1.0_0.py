import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    # read:
    print(struct.unpack('B', m[0:1])[0])
    # write:
    m[0:1] = struct.pack('B', 2)
</code>

