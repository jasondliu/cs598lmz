import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
But I get a <code>ValueError: mmap length is zero</code>. 
How to truncate a file and keep the mmap?


A:

I think you're looking for <code>mmap.resize</code>.
<code>m.resize(0)
</code>

