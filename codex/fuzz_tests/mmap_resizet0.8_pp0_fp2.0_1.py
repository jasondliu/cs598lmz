import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is not an empty list, as I expected, but <code>[0]</code>, which is the result of <code>bytes(1)</code>. Why <code>m[:]</code> returns a non-empty result while the file size is zero? Is this a bug?
The output of above code on Python 3.5.2 is <code>[0]</code>, while on Python 2.7.12 is <code>[]</code>.


A:

This is definitely a bug in Python 3.5.2. The Python 3.5 source code has a comment in the <code>mmap.mmap</code> method that contains a fix:
<code>if mmap_size == 0:
    # XXX(nnorwitz): issue18808 - Special case to workaround a bug in the
    # Windows mmap code.  When using mmap.MAP_PRIVATE, the mmap call
    # does not fill the memory with zeros.  The workaround is to
    # specify a mmap size greater than 0.  If size is 0, we will just

