import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read())
    m.close()
</code>
output:
<code>b'\x00'
</code>
I expect the output to be <code>b'\x02'</code>, but it's not.
If I try to write to the file using <code>f.write(bytes(2))</code>, it works.
I'm using Python 3.6.5.

