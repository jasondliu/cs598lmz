import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), length=0)
    m[0] = bytes(2)
    m.close()
</code>
What surprises me is that, despite the length being specified as 0, the file grows to the size of 0x100. Is this caused by the internal algorithms of mmap? Or is there something wrong with my usage?
If I use the second parameter as -1, I get a <code>ValueError: mmap length is negative</code>.
If I use the second parameter as utils.PAGESIZE or actual file size, then the problem disappears.
I am using a Python 3.6 under macOS Sierra.

