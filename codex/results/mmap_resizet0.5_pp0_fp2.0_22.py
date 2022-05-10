import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()

with open('test', 'rb') as f:
    a = f.read()
    print(a)
</code>
The output is:
<code>b''
b'\x01'
</code>
I would expect to get <code>b'\x01'</code> and <code>b''</code>, but instead I get <code>b''</code> and <code>b'\x01'</code>.
Is there a way to make the mmap object not to cache the data?


A:

I think you're misunderstanding the purpose of <code>mmap</code>.
<code>mmap</code> creates a memory map (a pointer to a region of memory) which is backed by the file.  It's a way to access the file without needing to read it into memory.  It's not a cache.  The memory map will be updated when you write to the file, and the file will be updated when you write to the memory map.
If you want to read the file, use <code>read</code>.  If
