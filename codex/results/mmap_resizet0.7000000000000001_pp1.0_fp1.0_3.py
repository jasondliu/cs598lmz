import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # reads beyond the end of the file
    print(a)
</code>
This is the output I get
<code>b'\x00'
</code>
Why am I getting a <code>b'\x00'</code>?


A:

Truncating a file does not change the size of the underlying mmap object. It just keeps the file open and allows you to write to it.

