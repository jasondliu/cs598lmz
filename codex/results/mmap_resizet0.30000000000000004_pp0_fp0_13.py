import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b'\x00'</code>
I would expect the output to be <code>b'\x01'</code>
Why is this?


A:

<code>mmap</code> is a view into a file.  If you truncate the file, the view is still the same size, but the data is gone.  You can't read it.  You can't write to it.  You can't resize it.  You can't do anything with it.  It's a view into a file that doesn't exist anymore.  You can't even close it.  You have to <code>munmap</code> it.

