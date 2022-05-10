import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x01')
    m[0] = b'\x02'
    m.resize(128)
    m.write(b'\x03')
</code>
what is the difference between:
<code>m.write(b'\x01')
</code>
and
<code>m[0] = b'\x02'
</code>
What is the effect of
<code>m.resize(128)
</code>
?
It seems they are different to each other. And resize was not successful, but there was no error message. And the code just stopped right there. What I'm trying to do is create a file with a small amt of data, then later write it with some more data. The purpose is to have a bunch of files all with the same file size.


A:

<code>mmap.mmap</code> is a python wrapper of the <code>mmap</code> C function.
For a more detailed explanation, see here: docs.python.org/3/library/mmap.html#mmap
