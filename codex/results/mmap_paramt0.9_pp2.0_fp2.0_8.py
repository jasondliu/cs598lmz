import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0

with open('test', 'rb') as f:
    print(f.read(1))
</code>
I expected it to print out <code>0</code> but it prints out <code>1</code>. Why?


A:

<code>mmap</code> has a buffer that keeps the changes. You need to explicitly <code>flush</code> it before the changes will take effect.
<code>m.flush()
</code>

