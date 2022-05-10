import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
</code>
In the above example, I'm using the <code>write</code> method of the <code>mmap</code> object to change the value of the byte at position 0 to 2. However, when I try to access the file using the <code>read</code> method of the <code>mmap</code> object, I get the original value of 1.
<code>&gt;&gt;&gt; m.read(1)
b'\x01'
</code>
I'm not sure what I'm doing wrong.


A:

You need to call <code>mmap.flush()</code> before closing the file.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.flush()
</code>

