import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expected <code>a</code> to be <code>b''</code>, but instead got <code>b'\x01'</code>.
My question is why this happens, and how I can get <code>a</code> to be <code>b''</code>?
I'm on Windows 10 if that makes a difference.


A:

I think you're misunderstanding what a memory map does. It's a virtual view of the file contents in memory. It doesn't contain a copy of the file contents. When you truncate the file, you're not truncating the memory map.
If you want to truncate the memory map, you can use <code>m.resize(0)</code>.

