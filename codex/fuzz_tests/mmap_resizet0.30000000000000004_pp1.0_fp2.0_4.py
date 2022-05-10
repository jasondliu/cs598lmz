import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I expect the output to be <code>b'\x01'</code> but it is <code>b''</code>.
I have tried this on both Windows and Linux.
Is this a bug or am I doing something wrong?


A:

I think you are doing something wrong.
<code>f.truncate()</code> truncates the file to zero length.
<code>m[:]</code> returns the whole content of the memory-mapped file, which is now empty.

