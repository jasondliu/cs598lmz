import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    m.flush()
    m.close()

with open('test', 'rb') as f:
    print(f.read())

os.remove('test')
</code>
If this is the intended behavior, what would be the best way to have atomic operations writing to the file through mmap?


A:

First of all, be aware that map doesn't cover whole file and maybe it's not enough space so you should grow the map instead of letting it fail without warning or raising exception just because doesn't fit.
Second, once you have enough space, instead of writing single byte at a time, you should use assign method to increase the performance:
<code>m = mmap.mmap(f.fileno(), 0)
m.resize(7)
m.assign(bytes(2))
</code>

