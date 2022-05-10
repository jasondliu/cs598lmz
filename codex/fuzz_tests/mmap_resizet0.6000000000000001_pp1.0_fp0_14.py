import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I would like to read the data in the file even if the file is truncated.


A:

You could read the file up to the maximum size before truncating it.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    f.truncate()
    print(a)
</code>

