import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 2
</code>
Edit:
    I made a copy-paste mistake, I accidentally added mmap.mmap(f.fileno(), 0).
    Thanks @eyquem for pointing it out.

