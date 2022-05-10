import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    pass
</code>
I thought this would result in an error, but it does not. The code works fine and <code>a</code> is an empty <code>bytes</code> object.
Why is that?


A:

https://github.com/python/cpython/blob/master/Modules/_io/fileio.c#L716-L722
<code>m = mmap.mmap(f.fileno(), 0)
f.truncate()
</code>
Above is equivalent to
<code>m = mmap.mmap(fileno, 0)
truncate(fileno, 0)
</code>
<code>truncate</code> is equivalent to <code>ftruncate</code>, which is defined in the POSIX standard. The key text in <code>truncate</code> is
<blockquote>
<p>The file is opened if necessary, and <em>other than when opening the file, any file descriptor for the file must be derived from a file descriptor that was returned by a successful call to open(), creat(), dup(),
