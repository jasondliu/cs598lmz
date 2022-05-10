import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code gives me a <code>ValueError: mmap offset is greater than file size</code> error.
I have tried to use <code>m.resize(0)</code> and <code>m.close()</code> before <code>f.truncate()</code> but it didn't help.
How can I truncate the file and keep the mmap object valid?


A:

<code>mmap</code> is not designed to work with files that change size.  It is designed to work with files that are fixed in size.  You can't resize the file and keep the <code>mmap</code> object valid.  You need to close the <code>mmap</code> object, truncate the file, and then create a new <code>mmap</code> object.

