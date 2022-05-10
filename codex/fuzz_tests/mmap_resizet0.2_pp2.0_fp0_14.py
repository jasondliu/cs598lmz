import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I would expect <code>a</code> to be an empty byte array, but it is not.
I have also tried to use <code>m.flush()</code> and <code>m.close()</code> before truncating the file, but it didn't help.
What am I doing wrong?


A:

You can't truncate a file while it's mapped.  You have to unmap it first.

