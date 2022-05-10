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
I would expect the output to be <code>b'\x01'</code>.
Is this a bug in Python or am I doing something wrong?


A:

<code>f.truncate()</code> truncates the file to 0 bytes.
<code>m[:]</code> returns the entire contents of the memory-mapped file.
Since the file is now empty, the entire contents of the memory-mapped file is empty.

