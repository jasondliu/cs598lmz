import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get this error: <code>TypeError: truncate() argument must be None or &gt;= 0, not tuple</code>. It seems that <code>truncate()</code> works on the file object <code>f</code>, while <code>[:]</code> also accesses it through the <code>m</code> variable.
To work around this problem, I tried to close <code>m</code> or <code>f</code> inside the context. But that does not work, as those objects are not scoped.
What's the smartest way to achive this?
I could close <code>m</code> outside the context and reopen it within (probably simpler), but I'd like to do it all within a single context.


A:

This actually seems to be a bug in Python 3.6.0.  The relevant logic in <code>fileno()</code> should raise an exception if the file is not open.  But in your code, the file is being closed by a context manager, and so Python simply assumes that the underlying <code>_io.BufferedIOBase</code
