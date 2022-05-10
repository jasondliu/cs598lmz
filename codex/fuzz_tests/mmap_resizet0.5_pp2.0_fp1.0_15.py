import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # This is what I want to avoid.
</code>
Is there a way to avoid reading the whole file? I don't want to read the whole file because it is going to be a large file.


A:

You can't.
The only way to avoid reading the whole file is to not use <code>mmap</code>.

