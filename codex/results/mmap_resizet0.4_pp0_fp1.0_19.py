import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)
</code>
The output is an empty list.
If I change the code to the following:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    a = f.read()

print(a)
</code>
The output is <code>b''</code>.
So in the first case, the <code>mmap</code> object is not updated after the file is truncated. In the second case, the <code>file</code> object is updated.
Why?

