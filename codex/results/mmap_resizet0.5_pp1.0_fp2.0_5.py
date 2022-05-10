import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line gives me a <code>ValueError</code>:
<code>ValueError: mmap length is zero
</code>
How can I make this work? I'm using Python 3.6.


A:

<code>mmap</code> does not support truncation.
You can call <code>mmap.resize()</code> to resize the mapping to a smaller size, but that's it.
If you need to truncate the file, you'll need to close the mapping and reopen it:
<code>m.close()
f.truncate()
m = mmap.mmap(f.fileno(), 0)
</code>

