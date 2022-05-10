import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

    m.write(b'\x02')
    m.seek(0)
    print(binascii.hexlify(m.read(1)) == b'02')
</code>
If the file already contains data, you can remove the 0 in mmap.mmap and it will map the rest of the file.
As the mmap goes out of scope, it will be automatically closed.

