import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line gives <code>ValueError: mmap offset is greater than file size</code>.
It appears that <code>mmap.mmap</code> doesn't see the new file size. Is there a way to make it work?
I know that I can create the <code>mmap</code> object after the <code>f.truncate()</code> line, but I'm looking for a more elegant solution, as my code would be more complicated than this example.


A:

I found a workaround:
<code>m = mmap.mmap(f.fileno(), 0)
f.truncate()
m.close()
m = mmap.mmap(f.fileno(), 0)
</code>

