import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
a is an empty bytestring, even though when I look in the file, there is data. What is going on? The big picture is that I want to be able to modify a file, but I want to keep a reference to a part of it so I can see what I changed. I'm trying to create unit tests for something that modifies a file, and I want to see what was changed. I thought mmap would work for this, but it doesn't seem to.


A:

mmap() stays valid until the process exits.  It doesn't get invalidated when the file changes size.
man mmap mentions "the file may be extended or shrunk by writing".  That's different from the file size changing: new bytes in the file are provided through the mmap'ed window.
However, the manpage goes on to state "mmap() does not read beyond the end of the file (beware of some older BSD implementations which do).  In particular, a write() past the end of the file is not visible through the mmap'd region.  It is unspecified whether changes made to the file after the mmap() call are visible in the mapped region
