import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I want to get an empty byte array (i.e. <code>b''</code>), but instead I get <code>b'\x01'</code>.
How can I get an empty byte array?


A:

The file has been truncated by <code>f.truncate()</code>. When you read from <code>m</code>, the byte has been written on the file (you can check this with the file manager), but it has been removed from the mmap, so you can't see it in the memory.
In fact, if <code>truncate()</code> is called after the mmap then it is alright to read from the mmap. This happens because <code>truncate()</code> changes the size of the mapping and as long as the size stays the same, you can read from the mmap.
This is how it should be done.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    f.truncate()
   
