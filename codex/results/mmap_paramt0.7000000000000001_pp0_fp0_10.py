import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(2)

with open('test', 'rb') as f:
    print(f.read())

# 1
</code>
Note: The <code>mmap.mmap</code> object is not garbage collected when the context manager exits, and you should call <code>mmap.mmap.close</code> explicitly when you are finished using it.

