import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
The last line will raise <code>ValueError: mmap closed or invalid</code>. I think the <code>truncate</code> method will change the size of the file. So the <code>mmap</code> object is invalid.
So I have two questions:

Why the <code>ValueError</code> raised?
How to truncate the file and still keep the <code>mmap</code> object valid?



A:

You need to call <code>mmap.resize</code> after <code>truncate</code> to resize the mapped object.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(f.tell())
    a = m[:]
    m.close()
</code>

