import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this example, I would expect <code>a</code> to be an empty string, but it is actually <code>b'\x01'</code>.
This is very surprising to me, and it is not documented anywhere. How can I make the expected behavior work? I don't want to use <code>mmap.ACCESS_WRITE</code> because I don't want to modify the file (I want to keep it as is).

