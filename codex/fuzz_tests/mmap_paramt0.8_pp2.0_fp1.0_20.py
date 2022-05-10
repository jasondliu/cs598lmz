import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = bytes(5)
    print(m.read(1))
</code>
Prints <code>5</code>.
Slightly larger example:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = bytes(5)
    m.seek(0)
    m.write(bytes(6))
    with open('test2', 'w') as f2:
        f2.write(m.read())
</code>
Now, <code>test</code> contains <code>"555555"</code> and <code>test2</code> contains <code>"666666"</code>.
For the record, I'm using Python 3.3 on Windows 7.

