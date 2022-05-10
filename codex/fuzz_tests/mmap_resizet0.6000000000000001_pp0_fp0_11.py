import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

with open('test', 'w') as f:
    f.write(a)
</code>
You can easily modify the code to read the file in chunks and write it to a new one, instead of keeping it in memory (I'm not sure if it's possible to read from the mmap).

