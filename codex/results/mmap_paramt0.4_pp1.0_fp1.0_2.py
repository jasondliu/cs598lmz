import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m[0] = b'\x00'
    print(m)
    m.close()
</code>
It prints:
<code>&lt;mmap.mmap object at 0x7f8c8e08d0c8&gt;
&lt;mmap.mmap object at 0x7f8c8e08d0c8&gt;
</code>
I expected the second print to be <code>&lt;mmap.mmap object at 0x7f8c8e08d0c8&gt;\x00</code>.
Why is it not?


A:

<code>mmap.mmap</code> is a memory-mapped file object.
It doesn't have a <code>__repr__</code> method, so it's just printing the default representation of the object, which is <code>&lt;mmap.mmap object at 0x7f8c8e08d0c8&gt;</code>.
If you want to see the contents of the file, you can do
