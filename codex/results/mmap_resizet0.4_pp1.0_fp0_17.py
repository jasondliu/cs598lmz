import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I would expect the output to be <code>b'\x01'</code> but instead it is <code>b''</code>.
Why is that?


A:

The mmap object is not aware that the file has been truncated. 
The mmap object only knows about the size of the file when it was created.
You can use the <code>mmap.resize()</code> method to resize the mmap object.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    a = m[:]
    print(a)
</code>

