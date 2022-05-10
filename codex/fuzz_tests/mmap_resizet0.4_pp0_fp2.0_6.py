import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I get <code>ValueError: mmap offset is greater than file size</code>.
I am using Python 3.5.2 on Windows 7.
I want to use <code>mmap</code> to read a file, then truncate it, then write it back.
I don't want to use <code>mmap.resize</code> because it's not available on Windows.
I don't want to use <code>mmap.ACCESS_WRITE</code> because I don't want to overwrite the file.
I don't want to use <code>mmap.ACCESS_COPY</code> because I don't want to create a copy of the file.
I don't want to use <code>mmap.ACCESS_READ</code> because I want to use <code>mmap.resize</code> to truncate the file.
I don't want to use <code>mmap.ACCESS_DEFAULT</code> because I want to use <code>mmap.resize</code> to truncate the file.
I don't want to use
