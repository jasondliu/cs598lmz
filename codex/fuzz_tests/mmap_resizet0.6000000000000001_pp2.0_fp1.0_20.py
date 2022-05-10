import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This gives me an <code>IndexError: mmap slice is bigger than file size</code> which is understandable.
My question is: why doesn't the <code>mmap</code> object see the file size has changed? Is there a way to make it see?


A:

Here's a way to do it, but it's a bit of a hack and I'm not sure it's a good idea.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
</code>
The function <code>resize</code> is undocumented, but it's present in the source code.

