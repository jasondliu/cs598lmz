import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
It fails on <code>a = m[:]</code> with <code>ValueError: memory block is being resized</code>. Is it a bug in Python or am I missing something?
Update
I'm using Ubuntu 14.04 with Python 3.4.0.


A:

I've just tried with python 2.7.10 and I get the same exception.
For me it looks like a bug, but I'm not sure.
What is certain is that there isn't a real error in your code, because you're not resizing the memory block.
I think that the only thing that you can do is to report the bug.

