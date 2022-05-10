import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
</code>
Can someone explain why this is?


A:

The reason is because you didn't specify the size of the file.
The following works as expected:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)  # specify size
    m.seek(0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
</code>

