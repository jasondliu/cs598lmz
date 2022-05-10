import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # segfaults here
</code>
EDIT:
Turns out this is only a bug in 2.7.13 and earlier. It was fixed in 2.7.14. https://bugs.python.org/issue29387

