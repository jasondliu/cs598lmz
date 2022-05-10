import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read_byte())
    m.seek(0)
    m.write_byte(bytes(2))
    m.seek(0)
    print(m.read_byte())
    m.close()

with open('test', 'r') as f:
    print(f.read(1))
</code>
The output I am getting is:
<code>1
2
2
</code>
While I am expecting:
<code>1
2
1
</code>
Where am I wrong?
Please note that I am using Python 3.6.


A:

I am pretty sure that the problem is that <code>read_byte</code> and <code>write_byte</code> both expect <code>byte</code> objects and not <code>int</code>.
This code works:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.
