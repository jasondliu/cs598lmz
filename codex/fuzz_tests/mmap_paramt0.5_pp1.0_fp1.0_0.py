import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())

with open('test', 'r+b') as f:
    print(f.read())
</code>
The output is:
<code>b'\x00'
b'\x02'
</code>
Why is the first read returning <code>b'\x00'</code> instead of <code>b'\x02'</code>?
If I change the code to:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())
</code>
I get:
<code>b'\x02'
</code>
I'm on Python 3.6.5.


A:

It's a buffering issue.
<code>
