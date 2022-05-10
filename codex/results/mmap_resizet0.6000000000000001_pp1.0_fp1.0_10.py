import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(len(a))
</code>
I'm getting a <code>ValueError: cannot mmap an empty file</code>.
How can I get the data from the file after truncating?
I'm using Python 3.5.2.


A:

You can't.
<code>mmap</code> is a virtual mapping of a file to a memory block. If you truncate the file, the memory block becomes invalid. You need to <code>close</code> the <code>mmap</code> object, then re-open it.

