import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Error:
<code>ValueError: mmap can't retrieve size of closed file
</code>
My question is: Why can't I truncate the file?


A:

because the file descriptor is still being held by the mmap object.  If you want to truncate you must close the mmap object first.

