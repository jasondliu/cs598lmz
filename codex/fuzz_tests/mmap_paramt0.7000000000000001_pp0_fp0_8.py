import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[1:] = bytes(2)
    m.close()

with open('test', 'rb') as f:
    print(repr(f.read()))
</code>
The above prints <code>b'\x00\x00'</code> as expected. However, if I change <code>with</code> to <code>as</code>,
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[1:] = bytes(2)
as m:
    m.close()

with open('test', 'rb') as f:
    print(repr(f.read()))
</code>
the above prints <code>b'\x01\x01'</code> which is not what I expected.
What is going on here?


A:

<code>as</code> is a keyword in a <code>
