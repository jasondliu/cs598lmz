import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I expect <code>a</code> to be an empty <code>bytes</code> object. However, it has length 1.
I know I can workaround this by using <code>m.close()</code> and then truncating the file. Is this a bug, or am I missing something?


A:

I think this is a bug.  I've filed an issue: https://bugs.python.org/issue32499
If you look at the implementation of <code>mmap.mmap</code>, you can see that it opens the file anew in readonly mode, and does not get the size from the existing fd:
<code>    self.fd = os.open(filename, os.O_RDONLY)
    try:
        self.size = os.path.getsize(filename)
        [...]
        if self.size == 0:
            raise ValueError("empty file")
</code>
So it is truncated to 0 bytes by your <code>f.truncate()</code>, but the new fd is still open and looking at the old
