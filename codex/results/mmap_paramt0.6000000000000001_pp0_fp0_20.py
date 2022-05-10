import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = 2
    m.flush()
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>


A:

The <code>mmap</code> module is designed to work with binary data (bytes) and not with character data (strings).
If you want to work with character data, you should use <code>mmap.mmap.read</code> and <code>mmap.mmap.write</code> methods instead of the indexing operator.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    m.write(b'2')
    m.flush()
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
