import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
If you read through the mmap module documentation, you will see that mmap objects operate entirely on the virtual memory of the process; <code>mmap.mmap</code> does not read a file when called. This means that, if you open a new mmap object after truncating a file, but with the same file descriptor, the mmap object will have <code>limit</code> set to the file size before the truncate.
Once a mmap object is created, it will not change. So when <code>m.close()</code> is called, and <code>m</code> is set to the empty slice <code>m[:]</code>, the bytes that were in <code>m</code> before <code>f.truncate()</code> are returned.

