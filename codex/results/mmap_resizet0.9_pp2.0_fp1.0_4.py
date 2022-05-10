import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
# First time a is empty, as expected.

# Run again
with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
# But now a is not empty!
</code>
What on earth? Why is this happening and how can it be made to work properly?


A:

Documentation says:
<blockquote>
<p><em>mmap=mmap.mmap(fileno, length, tagname=None, access=mmap.ACCESS_DEFAULT, offset=0)</em></p>
<p>Open an existing file and create a new mmap object, as with <code>&lt;code&gt;mmap(fileno, length, access=mmap.ACCESS_DEFAULT, offset=0)&lt;/code&gt;</code>, but use the file size as the size of the mmap (and the <code>&lt;code&gt;offset=0&lt;/code&gt;</code>).</
