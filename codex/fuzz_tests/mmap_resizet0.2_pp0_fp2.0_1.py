import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is:
<code>b'\x01'
</code>
I would expect the output to be <code>b''</code>.
Why is this?


A:

The <code>mmap</code> object is still pointing to the same memory location, even though the file has been truncated.
If you want to truncate the file and have the <code>mmap</code> object reflect the change, you need to call <code>mmap.resize</code> after truncating the file:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
    print(a)
</code>

