import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    print(m[:])
    m[0] = bytes(2)
f.close()
</code>
result is: <code>b'\x01'</code>.Why there is no <code>b'\x02'</code> instead?


A:

mmap does not automagically update the in-memory copy for you. You have to call m.flush() to do that.
Also, m[:] is a Python object and thus a copy, so you can't assign to it. Doing m[0:1] will return a bytes object that you can assign to, though.

