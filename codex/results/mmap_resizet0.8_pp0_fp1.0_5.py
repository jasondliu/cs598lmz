import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m[:5]
    c = m[5:]
</code>
when <code>f.truncate()</code> is called, <code>a</code>, <code>b</code>, <code>c</code> are all set to none.  I would have expected <code>a</code> and <code>b</code> to not be none.  Is there any way to get the expected behavior?  Or is there some way to fix this?  Or is it a bug in the module?


A:

I think this is a bug, I've filed a ticket here: https://bugs.python.org/issue30696

