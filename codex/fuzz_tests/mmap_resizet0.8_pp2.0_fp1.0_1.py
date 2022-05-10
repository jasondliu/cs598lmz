import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line of code throws an exception
<blockquote>
<p>mmap.error: [Errno 22] Invalid argument</p>
</blockquote>
If I do
<code>m.flush()
m.close()
</code>
before the truncation, everything is fine.
It seems that the mmap object is not aware of the truncation, but it's unclear to me why it's not aware, or if it's desirable to be so.
Is this a bug, or am I doing something wrong?
I'm using Python 3.5 and Linux 4.4.0-21-generic.

