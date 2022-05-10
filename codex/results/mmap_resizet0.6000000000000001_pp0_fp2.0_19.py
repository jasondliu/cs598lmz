import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I want to access the memory mapped data (a) after truncating the file, but I get:
<code>ValueError: mmap can't extend file to larger than 2GB
</code>
I know that the size of my file is smaller than 2GB, so I don't really understand what the problem is.

