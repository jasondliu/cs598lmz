import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
print(a)
</code>
I would expect the output to be <code>b'\x01'</code> but it actually prints an empty string. Why is this?


A:

The <code>mmap</code> object is backed by a memory map of the file. Once you call <code>f.truncate()</code>, the file is shorter and so there is no longer any memory mapped for the byte you're trying to read.

