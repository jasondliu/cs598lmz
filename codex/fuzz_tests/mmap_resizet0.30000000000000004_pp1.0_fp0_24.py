import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expected to get an empty byte string, but I get <code>b'\x01'</code> instead.
If I use <code>mmap.mmap(f.fileno(), 1)</code> instead, I get an empty byte string.
Why is that?


A:

The <code>mmap</code> object is not updated when you truncate the file.
The <code>mmap</code> object is a view of the file at a certain point in time. It is not updated when the file is changed.
You can use <code>mmap.resize</code> to resize the <code>mmap</code> object.
<code>m.resize(0)
</code>

