import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Here, <code>m[:]</code> raises <code>ValueError: memory mapping closed or invalid</code>.
I know that it is possible to reopen the file and map it again, but I am wondering if there is a way to keep the file mapped after truncating it.

