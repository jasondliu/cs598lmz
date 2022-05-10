import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This program prints an empty array.
Is there any way to access the mapped data after truncating the file?
I know that I can read the data before truncating the file, but my program will be working with the data after truncating it, so this solution doesn't help.
I could also save the data from the array to a new file, but I'm looking for a solution that doesn't require making any copies of the data.
I'm using Python 3.4.4 on Linux.


A:

I would say that this is not possible. 
There is a data access method called <code>mmap.resize</code> but it is not implemented on Linux in Python 3.4.4 (see https://docs.python.org/3/library/mmap.html#mmap.mmap.resize and https://docs.python.org/3.4/library/mmap.html#platform-specific-behavior) and the comment in the source code <code>mmap.c</code> says:
<blockquote>
<p>Only Windows has the equivalent of this call, so
