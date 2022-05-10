import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    c = 0
    for _ in m:
        c += 1

    print(c)
</code>
output:
<code>7
</code>
and
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    c = 0
    for _ in m:
        c += 1

    print(c)
</code>
output:
<code>0
</code>
It seems strange. 
Why reading from <code>mmap.ACCESS_READ</code> is not working?


A:

I think it's a bug. Here's a workaround.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.
