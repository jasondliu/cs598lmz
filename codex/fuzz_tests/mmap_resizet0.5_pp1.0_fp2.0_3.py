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
But I get the error:
<code>ValueError: mmap can't resize a read-only or copy-on-write (COW) mapped region
</code>


A:

You can't resize a file with a mmap open on it. It's not possible to change the size of the file while there's a mmap open on it.

