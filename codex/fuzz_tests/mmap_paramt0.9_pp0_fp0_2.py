import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = b'\x00'
</code>
The followings do not work:
<code>m[0:1] = b'0'
m[0:1] = '\x00'
</code>
Why are these last two cases not working?


A:

The type of the content of the mmap has to match the type of the content that is written. <code>0</code> and <code>'\x00'</code> are both strings, while <code>b'\x00'</code> is a byte string. You can also use an integer:
<code>m[0:1] = 0
</code>

