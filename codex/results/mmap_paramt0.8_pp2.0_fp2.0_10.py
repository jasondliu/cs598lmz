import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1024)
    m.close()
</code>
Or alternatively, a working, but cleaner way of doing it that can also be used in python3:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes([1]))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(1024)
    m.close()
</code>

