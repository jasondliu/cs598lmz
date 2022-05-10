import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises <code>ValueError: mmap offset is greater than file size</code> exception.
It seems that mmap doesn't like file truncation.
Is there any way to avoid this problem?


A:

That is because the <code>mmap</code> object is still tied to the old size.  Once you truncate, it's invalidated.  You need to call <code>m.close()</code> before <code>truncate()</code> if you want to keep the <code>mmap</code> object around.  Then you can create a new one with the correct size.

