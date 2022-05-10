import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
and it works fine, but I am wondering why Python doesn't handle the exception itself and throw it. Can anyone explain this to me?


A:

AFAIK, there is no explanation from the Python team, but the behavior is consistent with the Python philosophy of being explicit.
<blockquote>
<p>Explicit is better than implicit.</p>
</blockquote>
This is the zen of python.

