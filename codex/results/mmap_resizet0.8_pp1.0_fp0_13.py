import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
In this example <code>a</code> contains <code>b'\x00'</code> not <code>b'\x01'</code>.
Even if I change the code to:
<code>m = mmap.mmap(f.fileno(), 1)
</code>
I get <code>b'\x00'</code>.
Is there a way to get the original data back?


A:

The <code>mmap</code> will stay valid until it is explicitly closed or the process is terminated.
So in the above case <code>m[0]</code> is still <code>1</code>.
So to fix it we need to close the <code>mmap</code>:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.close()
    a = bytes(m)
</code>

