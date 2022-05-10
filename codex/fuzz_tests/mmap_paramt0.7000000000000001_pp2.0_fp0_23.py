import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(0)
    m.close()
</code>


A:

it should be 
<code>m[0] = 0
</code>
not
<code>m[0] = bytes(0)
</code>

