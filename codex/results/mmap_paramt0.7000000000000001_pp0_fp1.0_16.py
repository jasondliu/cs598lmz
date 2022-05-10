import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes([2])

with open('test', 'r+b') as f:
    print(f.readline())
</code>
This gives me:
<code>b'2'
</code>
If I try to use the <code>'w'</code> mode instead, I get a <code>ValueError</code>.


A:

I think you are looking for the <code>filename</code> argument of <code>mmap</code>:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with mmap.mmap(-1, 0, 'test') as m:
    m[0] = bytes([2])

with open('test', 'r+b') as f:
    print(f.readline())
</code>
Output:
<code>b'2'
</code>

