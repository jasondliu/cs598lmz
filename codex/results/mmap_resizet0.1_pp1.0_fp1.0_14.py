import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>.
I expected the output to be <code>b'\x01'</code>.
Why is the output <code>b'\x00'</code>?


A:

The <code>mmap</code> object is not updated when the file is truncated.  You can see this by printing the length of the <code>mmap</code> object:
<code>&gt;&gt;&gt; len(m)
1
</code>
The <code>mmap</code> object is updated when the file is resized, but not when it is truncated.  This is because truncating a file is a fast operation that doesn't require any disk access.  Resizing a file, on the other hand, requires disk access, so it's slower.

