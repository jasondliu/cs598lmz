import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises a <code>ValueError: mmap offset is greater than file size</code> error.
I assume this is caused by the fact that the mmap object still has a length of 1 byte, but the file has 0 bytes. However, I am not sure how to fix this.
I need the truncate because <code>file.write</code> resets the file to 0 bytes, while <code>file.truncate</code> actually leaves the file as is, which is what I need.

