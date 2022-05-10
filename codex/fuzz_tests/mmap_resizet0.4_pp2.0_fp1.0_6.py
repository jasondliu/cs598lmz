import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This results in <code>ValueError: mmap can't resize a readonly or copy-on-write memory mapping</code>.
I've tried <code>m.resize(0)</code> first, but that results in <code>ValueError: cannot resize a mmap that references a string</code>.
The only solution I've found is to close the <code>mmap</code> before truncating the file, but that's not really an option for me.
Is there a way to truncate a file with an open <code>mmap</code>?


A:

<code>mmap</code> requires the file to be open, so you can't truncate it.  You can, however, open a new file and <code>mmap</code> that.
<code>with open('test', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 0)
</code>

