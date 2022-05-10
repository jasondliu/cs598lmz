import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
In my version of python this crashes with an <code>OSError: [Errno 22] Invalid argument</code>, but I have thougths that it should dump the byte <code>1</code>.
What I am trying to achieve is a read only "memory map" of a file, without the the file being deleted.
Any idea?


A:

The first bit is that you need to set the length.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
</code>
The second is that in your case the file is being opened with <code>rb</code> and the file is being truncated, so when you do this:
<code>m[:]
</code>
you are reading the whole (empty) file.
If you are trying to create a read-only memory map, then you need to open in <code>r</code> mode.
Example of how to truncate a file and keep the data: https://stackoverflow.com/
