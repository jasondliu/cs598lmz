import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This code gives me <code>mmap.error: [Errno 12] Cannot allocate memory</code>.
I know that the problem is caused by the truncate because if I comment out that line, the code runs fine.
Why does the truncate cause the error?


A:

This is because the <code>mmap</code> object is holding on to the old size of the file, and when you call <code>m[:]</code>, it tries to map the old size of the file, which no longer exists.
To solve this, you can call <code>m.resize(0)</code> before calling <code>truncate()</code>.

