import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
print(a)
</code>
The code crashed, with "Buffer has been accessed" error.
I tested on Windows 10 and Windows 7. I can't find if there's restriction for using truncate() on a mmapped file in the docs of Python, but I can confirm that it can solve the problem. So I wonder is this a restriction in Python or Windows OS?

