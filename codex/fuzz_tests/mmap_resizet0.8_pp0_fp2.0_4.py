import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This throws:
<code>UnboundLocalError: local variable 'm' referenced before assignment
</code>
But if I add a local variable <code>m</code> and assign it <code>None</code> initially, the code works as expected. Why does this happen?
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = None
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>


A:

An assignment is an expression. This is what your first example amounts to:
<code>m = mmap.mmap(f.fileno(), 0)
a = m[:]
f.truncate()
</code>
So <code>m</code> gets assigned a value, then the value is read but not assigned to <code>a</code> and then the file is truncated. <code>m</code> is still assigned, but it
