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
Output:
<code>b'\x00'
</code>
The only thing I could come up with to fix this is to first create a new file of the desired size, then copy the original file to the new one, but I would like to avoid this if possible.

