import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

with open('test', 'r+b') as f:
    f.write(bytes(1))
    f.truncate()
    f.seek(0)
    b = f.read(1)

print(a)
print(b)
</code>
I was expecting that both a and b should be equal to b'', but the output of this script is:
<code>b''
b'\x00'
</code>
Why is that? Why does mmap.mmap() return something different than what f.read() returns?


A:

You have no idea how mmap works. Try to read about it.
<code>mmap.mmap</code> does not read files. It creates a mapping from the file to memory, which means that the data from the file is already in memory, and if you don't want to read it from the file, no file operations are done when you access the data.
After that, you truncated the file, but the mapping does not care about that, because it is already in memory.
<code>f.read</
