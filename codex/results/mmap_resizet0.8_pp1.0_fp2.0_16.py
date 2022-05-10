import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Running this on Python 3.2, 3.3 and 3.4 gives an <code>ValueError: mmap length is zero</code> exception. This is expected as the length of the mmap is set to 0 in <code>f.truncate()</code>.
However, running the same code on Python 2.6.6, I get an <code>IOError: [Errno 22] Invalid argument</code>. This is in contrast to what the mmap documentation says:
<blockquote>
<p>If the file is extended, the extra data is <strong>undefined</strong></p>
</blockquote>
[emphasis added]
In this case, the extra data seems to be exactly what was there before.
In my case, I'd like to be able to use mmap as a simple way to remove the data from the underlying file, as calling <code>f.truncate(0)</code> followed by <code>m.resize(0)</code> results in inconsistent behaviour depending on the platform.
Is this behaviour intentional? Is it documented somewhere? It looks to me like a bug.

