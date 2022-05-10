import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 0
    m.close()
</code>
This code works fine if the file is opened in write mode, but fails if the file is opened in read mode. I understand that this is because the mmap is read-only. But how can I make it writeable?
I can't use <code>mmap.ACCESS_WRITE</code> because I'm on Windows. I can't use <code>mmap.ACCESS_COPY</code> because it's not supported on Windows.
I don't want to open the file in write mode because I don't want to truncate the file.


A:

<code>mmap</code> is not the right tool for you. It is designed to allow you to treat a file as a memory-mapped array. It is not designed to allow you to change the file.
If you want to read a file and then write a file, use <code>open</code> and <code>write</code>.
If you want to change a file in-place, use <code>fileinput</code>.

