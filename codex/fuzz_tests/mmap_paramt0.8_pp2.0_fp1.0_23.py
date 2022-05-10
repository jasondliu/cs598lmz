import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 2)
    m[0] = b'\x00'
    m[1] = b'\xff'
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
Obviously this is not what I want. I want the second byte of the file to be replaced with 0xff. Why is that not happening?

