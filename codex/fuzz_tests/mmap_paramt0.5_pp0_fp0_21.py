import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))
    m.write(bytes(1))
    m.write(bytes(1))
    print(m[:])
    m.close()

with open('test', 'r+b') as f:
    print(f.read())
</code>
Output:
<code>b'\x01\x01\x01'
b'\x01\x01\x01'
</code>
I read the docs and it says:
<blockquote>
<p>The optional size argument specifies the size of the buffer. If omitted, the size will be the current size of the file when mmap is called.</p>
</blockquote>
I don't understand why the size of the buffer is 1, when I specify <code>0</code> as the size.


A:

The size argument is not the size of the buffer, but the size of the memory mapped region. If you want to map the whole file, use <code>0</code> as the size argument.

