import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
Oddly enough, this works on Windows, but not on Linux, saying the file is already closed. If I do either <code>f.truncate()</code> or <code>m.close()</code> after the other, it works.
I've tried enumerating all the possible combinations of opening modes and mappings, but it seems like this one combination just doesn't work.
Why? How can I work around this?
This is with Python 3.2.2 on Ubuntu.


A:

On Windows <code>mmap.mmap</code> uses <code>MapViewOfFile</code>. Restrictions on <code>MapViewOfFile</code> with <code>FILE_MAP_WRITE</code> are not the same as those with <code>PAGE_READWRITE</code> (which is the basis for the restriction that you can't resize the file).
Furthermore, the mmap module says (in the comments for its memory object) that the object should be closed before mapping another file to the same memory area. So, in that respect, you
