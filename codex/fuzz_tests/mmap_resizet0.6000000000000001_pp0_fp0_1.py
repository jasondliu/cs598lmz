import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
This code raises an exception:
<blockquote>
<p>ValueError: cannot mmap an empty file</p>
</blockquote>
How to avoid this exception?
If I increase the length of the file to 2, the code works fine.


A:

The length of the file is zero.  The first argument to <code>mmap.mmap</code> is the file descriptor, and the second is the length.  When you truncate the file, the length is zero.  Since you are using <code>mmap</code> in read-only mode, the length doesn't matter, but you have to tell <code>mmap</code> what length you have in mind.  The length doesn't have to match the actual length of the file; it can be larger.
<code>m = mmap.mmap(f.fileno(), 1)  # length is 1
</code>

