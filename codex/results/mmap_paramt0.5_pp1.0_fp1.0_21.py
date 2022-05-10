import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
This is not working.


A:

You are trying to write a byte (<code>bytes(1)</code>) to a file.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))
</code>
This is equal to <code>f.write(bytes([1]))</code> and writes a file with a single byte: <code>0x01</code>.
Then you try to write a byte to that byte:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = bytes(2)
</code>
This is equal to <code>m[0] = bytes([2])</code> and writes a byte <code>0x02</code> to the file.
In the end you have a file with <code>0x02</code> in it, which is exactly what you asked for.

