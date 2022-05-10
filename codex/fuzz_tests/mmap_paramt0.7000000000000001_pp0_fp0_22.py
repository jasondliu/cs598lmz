import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = 0
</code>
This works on Linux, but on Windows this fails with <code>ValueError: cannot modify read-only memory</code>.
I found that trying to open the file with <code>access=mmap.ACCESS_WRITE</code> fails on Windows on Python 3.3 but works on Python 2.7.
According to https://docs.python.org/3/library/mmap.html, <code>ACCESS_WRITE</code> is supposed to be supported on Windows (and other platforms as well). According to https://docs.python.org/2/library/mmap.html, <code>ACCESS_WRITE</code> should raise an exception if not supported. In both cases, I get an exception, but for different reasons.
What's going on? How do I get this to work on Python 3.3 on Windows?


A:

<code>ACCESS_WRITE</code> is supported on Windows in Python 3.3, but not on Python 3.2 or earlier.

