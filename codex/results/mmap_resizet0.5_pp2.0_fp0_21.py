import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
<code>IndexError: string index out of range
</code>
I expected <code>a</code> to be a byte array of length 0.
How do I make this work?


A:

In Python 3, <code>mmap.mmap()</code> takes a <code>length</code> argument, which is the size of the mmap.  You set it to 0, which means it can't read anything.  You need to use the file size:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), f.tell())
    f.truncate()
    a = m[:]
</code>

