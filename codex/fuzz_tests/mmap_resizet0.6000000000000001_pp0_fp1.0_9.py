import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
<code>a</code> is <code>b''</code> and I'm expecting it to be <code>b'\x01'</code>.

Is this a bug in <code>mmap</code> or am I using it incorrectly?
Is there a way to easily get around this?



A:

You should not call <code>f.truncate()</code> after creating the <code>mmap</code> object.
From the <code>mmap</code> docs:
<blockquote>
<p>The size of the map in bytes must be a multiple of the ALLOCATIONGRANULARITY (which is 64K on Windows). This is not checked by the module, but may result in a ValueError from the operating system if it is violated.</p>
</blockquote>
The following code works:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    f.truncate()
