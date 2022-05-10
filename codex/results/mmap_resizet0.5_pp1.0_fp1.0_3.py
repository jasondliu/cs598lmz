import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
I'd expect the output to be <code>b'\x01'</code> but instead I get <code>b''</code>
I'm using python 3.6.1 on OSX.


A:

Your mmap object is not aware that the file has been truncated. You can use <code>m.resize()</code> to resize the mmap object to the same size as the file:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
    print(a)
    m.close()
</code>

