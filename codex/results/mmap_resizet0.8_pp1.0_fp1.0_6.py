import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>


A:

If your goal was to get the same data in <code>a</code> whether or not the file was empty, you could just skip the truncate and close the file:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    m.close()
</code>
This will leave the file at its original size, with whatever data was in it before.

