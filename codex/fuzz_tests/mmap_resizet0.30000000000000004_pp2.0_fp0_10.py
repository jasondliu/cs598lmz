import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This results in an <code>OSError: [Errno 22] Invalid argument</code> on the last line.
I would expect that the memory map is still valid, because the file is still open.
Is there a way to make this work?


A:

You can't do that.  The mmap object is a view of the file at a particular point in time.  When you truncate the file, the mmap object is no longer valid.

