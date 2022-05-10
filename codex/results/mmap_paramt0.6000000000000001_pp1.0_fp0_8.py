import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    print(m[:])
    m.write(b'a')
    m.seek(0)
    print(m.read(1))
    print(m[:])
    m.close()
</code>
This gives me:
<code>b'\x01'
b'\x01'
b'a'
b'a'
</code>
So it looks like the <code>mmap</code> object is not unmapped when I close it, and that it's the <code>m.write(b'a')</code> that actually writes to the file.
Is there a way to map the file in read-only mode, so that any <code>m.write()</code> raises an exception?

