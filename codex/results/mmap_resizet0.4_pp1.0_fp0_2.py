import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expect to get an empty byte array, but I get a byte array with one element.
<code>b'\x01'
</code>
Why is that?


A:

<code>mmap</code> does not know about the truncation, because it does not know about the file object.
You can use <code>m.resize(0)</code> to resize the <code>mmap</code> object after truncating the file.

