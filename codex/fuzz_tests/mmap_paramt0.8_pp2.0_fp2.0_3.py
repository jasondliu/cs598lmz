import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
I expected that the file would have no content after the resize and no content after the file is closed, but the file still has 1 in it. How can I truncate the file size with mmap?
(Also, if you have a more compact way to write this, I'd be interested to see it.)


A:

AFAIK you can't do it with <code>mmap</code> because the python implementation seems to use <code>mremap</code> or <code>ftruncate</code> to resize the mmap. Both of these calls preserve file data. The man pages for <code>mremap</code> and <code>ftruncate</code>:
<blockquote>
<p>Any of the above methods may result in the creation of a sparse file (a "hole").  A read from a sparse area returns zero bytes.</p>
</blockquote>
To zero a file you can use the <code>os.
