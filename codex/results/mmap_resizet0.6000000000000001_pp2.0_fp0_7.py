import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m[:]
    print(a)
    print(b)
</code>
The output of this program is 
<code>b'\x01'
b''
</code>
I expected both of them to be <code>b'\x01'</code>.
Why is this happening and what can I do to get the desired effect?


A:

The solution to my problem was to use the <code>mmap.ACCESS_READ</code> flag.
The following code does what I want:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    f.truncate()
    a = m[:]
    b = m[:]
    print(a)
    print(b)
</code>
The output of this program is
<code>b'\x01'
b'\x01
