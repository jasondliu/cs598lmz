import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
The error I get is:
<code>mmap.error: [Errno 22] Invalid argument
</code>
I've tried various combinations of mode, but no luck.


A:

You need to open the file in text mode and use a unicode string.
<code>import mmap

with open('test', 'w') as f:
    f.write('1')

with open('test', 'r+') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = '\x00'
</code>

