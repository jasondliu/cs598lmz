import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
After running this code, variable <code>a</code> will get bytes array <code>b'\x01'</code>.
But if I replace 
<code>f.truncate()
</code>
with
<code>f.seek(0, 2)
f.truncate()
</code>
I get an exception
<code>ValueError: mmap offset is greater than file size
</code>
This is a good example where I need to do something like that:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.seek(0, 2)
    byte = f.read(1)
    f.seek(0, 2)
    f.truncate()
    m[:] = byte
</code>
But this code fails with error above.
I understand why it fails and why it's wrong to do that kind of things.
I need to know why does it fail in this exact example when I call <code>f.seek(0, 2)</code
