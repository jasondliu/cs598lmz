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
<code>b'\x00'
</code>
I thought that the content of <code>m</code> should be <code>b'\x01'</code>. Why is the output <code>b'\x00'</code>?

