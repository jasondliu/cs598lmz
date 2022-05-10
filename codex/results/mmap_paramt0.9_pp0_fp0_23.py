import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 50
    out = [x for x in m]

print(out)
</code>
This outputs [50]. However, if I change the 0 in <code>out = [x for x in m]</code> to 1, it outputs [0], as I would expect.
I found that I can "fix" this in a way by changing the <code>m = mmap.mmap(f.fileno(), 0)</code> to <code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)</code>. Then output is always [50] as I would expect.
My question is: why is the <code>0</code> treated as a <code>1</code> in this case?


A:

Use <code>mmap.ACCESS_READ</code> when you intend to read. <code>ACCESS_WRITE</code> implies <code>ACCESS_READ</code>.
From https://docs.python.org/3/library/mmap.html#mmap.ACCESS_READ
