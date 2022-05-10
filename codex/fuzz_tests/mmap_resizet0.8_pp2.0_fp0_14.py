import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
but it prints <code>b'\x00'</code>. 
How do I get <code>b'\x01'</code>?


A:

The problem seems to be that truncating the file is actually truncating the memory map, not just the file. So you may want to consider creating the map with length <code>0</code> and then resizing it:
<code>m = mmap.mmap(f.fileno(), 0)
m.resize(1)
</code>

