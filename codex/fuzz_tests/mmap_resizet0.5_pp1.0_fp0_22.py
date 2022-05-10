import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The code above will print <code>b'\x00'</code>.
I'm using Python 3.5.2.
How can I avoid this?


A:

I've managed to find a workaround.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    print(a)
</code>
This will print <code>b''</code>.

