import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect the <code>a</code> to be an empty string, but actually it is equal to <code>b'\x01'</code>.
Why does it happen? How can I fix it?


A:

You are correct that <code>a</code> should be an empty string. It's a bug in <code>mmap</code>.
You can work around the issue by not truncating the file; just write a shorter value to the file:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.write(b'')
    a = m[:]
</code>

