import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'2')
    m.seek(0)
    print(m.read(1))
    m.close()
</code>
This code will print <code>b'2'</code> to the console, but the file itself will still contain only <code>b'1'</code>.

