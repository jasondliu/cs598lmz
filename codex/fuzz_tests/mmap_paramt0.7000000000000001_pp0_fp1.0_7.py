import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'a')
</code>
The above code will have no output and still <code>test</code> file will be empty.
Why I can't write to <code>test</code> file using the <code>mmap</code>?


A:

<code>mmap</code> is a read-only view of your file. You can create a mutable view by passing <code>mmap.MAP_SHARED</code> and a length of <code>1</code> to <code>mmap</code> (the length is in bytes, not in chars):
<code>m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_WRITE)
</code>
Note that the file must be opened in write mode.

