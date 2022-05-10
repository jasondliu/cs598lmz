import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    print(m[0])
    print(ord(m[0]))
    m[0] = ord('b')
    print(m[0])
    print(ord(m[0]))
    m.close()
</code>
This is the result I get:
<code>b'\x01'
1
b'.'
46
</code>
The first thing to understand is that m[0] is a bytes object and not a string. So you can't just modify it like you would in a string.
You need to <code>ord</code> the bytes object to get a int representation of the first char, then you can change the value. Afterwards, you need to <code>chr</code> the int back to a string to get the value of the changed char.

