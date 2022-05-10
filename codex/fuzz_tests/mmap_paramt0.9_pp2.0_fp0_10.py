import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x02'
</code>
But instead of a byte <code>0x02</code> I get the byte <code>0x02</code> with some junk leftover at the end. I could write the file incrementally and just ignore the junk, but I'd rather overwrite the file.
Is there a way to overwrite the existing file while retaining the trailing junk (or trick the OS into believing that there is more file than there actually is)?

