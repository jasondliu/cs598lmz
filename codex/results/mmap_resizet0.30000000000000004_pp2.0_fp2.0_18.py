import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code works fine, but if I change the <code>truncate</code> line to <code>f.truncate(0)</code>, it fails with <code>ValueError: mmap length is greater than file size</code>.
Why does this happen?


A:

The problem is that you're trying to read from the <code>mmap</code> object after you've truncated the file.  The <code>mmap</code> object is still pointing to the same place in the file, but the file is now shorter.  You can't read past the end of the file.

