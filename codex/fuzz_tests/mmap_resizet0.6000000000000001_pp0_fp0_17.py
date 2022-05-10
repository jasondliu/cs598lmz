import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get a <code>ValueError: mmap offset is greater than file size</code>.
If I use <code>mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code> instead, I get a <code>ValueError: mmap can't resize a file on a FAT filesystem</code>.
I also tried making the file bigger before truncating it, but that didn't work either.
How can I get the data from the file?

