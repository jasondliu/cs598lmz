import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    
with open('test', 'wb') as f:
    f.write(bytes(0x44444444444444444444))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
</code>
The last <code>mmap</code> fails with <code>ValueError: cannot mmap an empty file</code>
Why? How can I work around this without having to create an empty file and truncate it by hand?
Edit: The use case is that I am using an mmap as a list, growing to decent size. Then I want to resize the file (and therefore the mmap too) to be able to do <code>m.extend(new_item)</code>.
So I don't need another <code>mmap</code> instance for the file, but for the same map that already exists.
Edit 2 The user pointed out that this can be done with a <code>mmap.resize</code>. This caused a new issue. I have an issue tracking that, but I don't know how to close
