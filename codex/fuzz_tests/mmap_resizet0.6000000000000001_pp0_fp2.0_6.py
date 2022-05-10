import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code raises an <code>ValueError: mmap length is zero</code> exception.
So I added the <code>m.resize(0)</code> line:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
    m.close()
</code>
Now there is no exception, but the <code>a</code> variable is not empty, though the file is empty.
<code>print(a)  # prints: b'\x01'
</code>
What am I doing wrong?


A:

You are using a <code>mmap</code> object that is created with a zero-length mapping. You then change the underlying file, but the <code>mmap</code> object is not updated.
You created a zero-length mapping:
<code>m = mmap.mmap(f.fileno(), 0)
</code
