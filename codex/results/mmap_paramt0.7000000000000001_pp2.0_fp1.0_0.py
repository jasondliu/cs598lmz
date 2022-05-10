import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(2)
</code>
[EDIT]
In a comment, you said:
<blockquote>
<p>I am trying to write a function that takes in a buffer and a file name then writes the buffer to the file. I want to do this without creating a new file then overwriting it.</p>
</blockquote>
In that case, you can use the <code>mmap.resize()</code> method, which "resizes the memory map and underlying file to the new size" (examples in the docs).

