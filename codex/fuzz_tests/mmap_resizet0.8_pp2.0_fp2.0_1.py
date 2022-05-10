import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This snippet shows that the view is still valid after the file is truncated to 0. Is it possible to get a list of all views open on a file/descriptor?


A:

Looks like there isn't. I checked the implementation of mmap module and unfortunately there is no way to get all views on a file / descriptor.

