import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
What I do not understand is that the offset is 0. Why does it raise the exception?


A:

I don't know the exact reason, but the problem is that you are using <code>m[:]</code> to read the whole file.
If you try <code>m[0:]</code> instead, it works.
<code>m[0:]
# b'\x01'
</code>

