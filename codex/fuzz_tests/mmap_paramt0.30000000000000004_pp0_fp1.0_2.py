import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
This code works, but I don't know why.
I think the <code>m[0]</code> is a <code>bytes</code> object, so the <code>m[0] = b'\x00'</code> should be <code>m[0] = bytes(b'\x00')</code>.
But when I change the code to this, it doesn't work.
<code>m[0] = bytes(b'\x00')
</code>
Why?


A:

<code>mmap</code> objects have a <code>__setitem__</code> method that accepts a <code>bytes</code> object and writes it to the file.
<code>m[0] = b'\x00'
</code>
is equivalent to
<code>m.__setitem__(0, b'\x00')
</code>
which is equivalent to
<code>m.__setitem__(slice(0, 1), b
