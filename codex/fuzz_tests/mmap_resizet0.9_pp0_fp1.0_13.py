import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Error happens on the last line, with <code>TypeError: invalid type comparison</code>.


A:

I don't see anything obvious that can cause a TypeError.
If you want to read the whole content of the mmapped file:
<code>m = mmap.mmap(f.fileno(), 0)
f.seek(0,2)  # to the end of the file
m.resize(f.tell())  # resize mmap to the actual size of the file
f.truncate()
</code>

