import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m.resize(5)
    print(m)
    m.close()
</code>
This gives the following error:
<code>mmap.error: [Errno 12] Cannot allocate memory
</code>
I tried to look into <code>mmap</code> source to find out how it is implemented and I found out that <code>resize</code> method calls:
<code>int Py_PROT_WRITE, Py_MAP_SHARED, self-&gt;fd, self-&gt;pos
</code>
So it looks like the problem is Python itself doesn't support resizing <code>mmap</code>. Any ideas how to achieve that?


A:

I think, you are looking for something like this:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m
