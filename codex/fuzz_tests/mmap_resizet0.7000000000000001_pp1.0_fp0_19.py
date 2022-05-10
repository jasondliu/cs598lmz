import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    b = [1]
    print(b)
</code>
The output is:
<code>b'\x01'
[1]
</code>
And <code>mmap</code> is not working anymore.
How can I get <code>mmap</code> working again?


A:

You need to call <code>mmap.resize</code> after you truncate the file:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
    print(a)
    b = [1]
    print(b)
</code>
Documentation: https://docs.python.org/3/library/mmap.html#mmap.mmap.resize

