import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
    # f.write(bytes(10)) # TypeError: write() argument must be str, not bytes
</code>
It was the <code>f.write</code> in the last line that I was trying to get working.

