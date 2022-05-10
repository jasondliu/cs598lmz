import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
you get a <code>ValueError</code>:
<blockquote>
<p>ValueError: mmap can't extend a mapped region</p>
</blockquote>
But if you do the same thing with Python 3.7
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
it works fine.
I have seen this behaviour on Ubuntu 18.04 with Python 3.6.7 and 3.7.2.
Is this a bug in Python 3.6?


A:

It seems that this is a bug in Python 3.6 which has been fixed in Python 3.7.
This is the relevant pull request: https://github.com/python/cpython/pull/9012

