import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I would expect the output to be <code>b'\x01'</code>, but instead I get <code>b''</code>.  Is this a bug in <code>mmap</code> or am I doing something wrong?

