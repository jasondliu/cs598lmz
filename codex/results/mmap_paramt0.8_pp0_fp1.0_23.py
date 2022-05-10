import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(5))
    m.seek(0)
    print(m.read(5))
    m.close()
</code>
Output:
<code>'\x00\x00\x00\x00\x00'
</code>
I would like it to be <code>'\x01\x05\x05\x05\x05'</code>, which is what I get when I use <code>'w+b'</code> in the open statement.  Is there a way to achieve this without using <code>'w+b'</code>?
Edit: I am open to using other modules.


A:

For those still looking for an answer, the following works
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.seek(0)
    m
