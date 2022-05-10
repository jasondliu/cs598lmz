import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The file will not get truncated. I need to use <code>mmap.resize</code> to resize the memory map.
This is really annoying, because I want to use file locking, but I need the file to get truncated so that other processes will not get errors.
Is there a way to make the <code>mmap</code> to automatically resize when a file gets truncated?

