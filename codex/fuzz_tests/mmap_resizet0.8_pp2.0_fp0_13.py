import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print 'a:', a
    print 'len(a):', len(a)
</code>
output:
<code>a: �
len(a): 1
</code>
a is not empty, it should be [].
Why?
=====update=====
I test it on Linux.
I think in windows it works right.


A:

<code>a</code> is not empty. <code>m</code> is a mmap of the file, which has not been truncated. <code>a</code> is just the bytes of that mmap. The <code>m[:]</code> doesn't read the file, it just returns the bytes of the mmap. The file is not changed until you call <code>m.flush()</code>. Executing <code>f.truncate()</code> on the file after the mmap has been changed but not flushed is undefined behavior.

