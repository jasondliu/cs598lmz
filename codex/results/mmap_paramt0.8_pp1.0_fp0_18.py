import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:len(bytes(1))] = bytes(1)
    m.flush()
    m[0:len(bytes(2))] = bytes(2)

with open('test', 'rb') as f:
    print(f.read())
</code>
Result:
<code>b'\x01'
</code>
So it appears that <code>mmap.flush</code> is a no-op. If true, why is this? I was expecting that the second <code>bytes</code> object to be written.
Python 3.5.2, Linux 4.10.0-28-generic, Ubuntu 16.04.2 LTS

