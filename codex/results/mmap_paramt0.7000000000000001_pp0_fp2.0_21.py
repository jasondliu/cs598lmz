import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m[:] = b'\xff'
    print(m)
</code>
output:
<code>&lt;mmap.mmap object at 0x000000000578FBE0&gt;
&lt;mmap.mmap object at 0x000000000578FBE0&gt;
</code>
I don't understand why the <code>mmap</code> object doesn't change after the <code>m[:] = b'\xff'</code> statement.


A:

You are printing the mmap object, which is the same object as before. The file itself was updated, you can see this if you print the file contents.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    m[:] = b'\xff'
    print(m)
    print(f.read())
</code>
Output:

