import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
On Windows 10 64bit, Python 3.7 64bit:
<code>b'2'
</code>
On Ubuntu 18.04 64bit, Python 3.6 64bit:
<code>b'\x0e'
</code>
So here, with <code>mmap</code> the expected behavior appears to be platform dependent.

