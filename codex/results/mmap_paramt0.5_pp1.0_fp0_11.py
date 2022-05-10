import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'
    m.close()
</code>
I would expect the file to contain the byte 2, but it still contains the byte 1.
The same happens when I use the <code>mmap</code> module directly:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with mmap.mmap(open('test', 'r+b').fileno(), 0) as m:
    m[0] = b'2'
</code>
I can't figure out what I'm doing wrong.
I'm using Python 3.6.8 on Windows 10.


A:

You need to call <code>mmap.flush()</code> to write the changes to the file.

