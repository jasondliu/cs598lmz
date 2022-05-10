import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    m.close()
</code>
The <code>resize</code> call is supposed to truncate the file, but it doesn't.
I'm using Python 3.3.3 on Ubuntu 12.04, 64-bit.


A:

The resize method sets the file size, it doesn't truncate the file. It seems you want to truncate the file, you could use f.truncate(0) or os.ftruncate(f.fileno(), 0) for that.

