import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code>.
If I open <code>test</code> with <code>'a+b'</code> instead of <code>'r+b'</code> the error doesn't raise.
I read the <code>mmap</code> documentation and I don't understand why it raises.

