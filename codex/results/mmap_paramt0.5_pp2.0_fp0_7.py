import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(2)
    m.write(bytes(1))
</code>
It works fine on my machine, but it seems that it's not guaranteed to work:
<blockquote>
<p>The underlying file size cannot be expanded, and the data cannot be moved beyond the current end-of-file.</p>
</blockquote>
I don't understand why it should not work. The underlying file is expanded, and the data is not moved beyond the current end-of-file.
Is there a way to do this in a more portable way?


A:

The documentation is wrong. The underlying file size can be expanded.

