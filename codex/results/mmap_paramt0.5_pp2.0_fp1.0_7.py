import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
I get an error <code>TypeError: an integer is required (got type bytes)</code>
I tried to use <code>m[0] = bytes(2)[0]</code> but then I get <code>TypeError: 'int' object is not subscriptable</code>
I also tried to use <code>m[0] = int.from_bytes(bytes(2), byteorder='little')</code> but then I get <code>TypeError: an integer is required (got type int)</code>
I tried to use <code>m[0] = int.from_bytes(bytes(2), byteorder='little')[0]</code> but then I get <code>TypeError: 'int' object is not subscriptable</code>
I tried to use <code>m[0] = int.from_bytes(bytes(2), byteorder='little').to_bytes(1, byteorder='little')
