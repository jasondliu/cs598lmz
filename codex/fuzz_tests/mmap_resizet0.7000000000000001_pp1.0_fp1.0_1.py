import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code gives me a <code>ValueError: mmap offset is greater than file size</code> exception. I think it should not as the file size is 1 byte and the offset is 0.
I'm using python 3.4.4 on Ubuntu 18.04.
EDIT:
I did the same thing with python 3.5.2 on Ubuntu 17.10 and everything works fine.

