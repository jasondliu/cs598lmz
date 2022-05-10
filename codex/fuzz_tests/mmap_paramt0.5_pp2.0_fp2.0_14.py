import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = bytes(2)
    print(m[0])
    m.close()

with open('test', 'r+b') as f:
    print(f.read())
</code>
The output is:
<code>1
2
2
</code>
The byte written to the <code>mmap</code> is written to the file.

