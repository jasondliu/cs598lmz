import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
I understand that <code>mmap</code> is using file descriptor, but I don't understand why it is not updated after <code>truncate</code>.
I also tried to use <code>os.ftruncate</code> instead of <code>truncate</code>, but it didn't help.

