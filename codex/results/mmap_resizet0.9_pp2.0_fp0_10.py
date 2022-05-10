import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect that <code>a</code> would be <code>bytes(1)</code>, but when I print out <code>a</code>, it's just <code>b''</code> - an empty byte literal. 
Is it possible to read the contents after I have truncated the file?
What I'm trying to do with this code is ensure that I don't have trailing bytes after I truncate the file.

