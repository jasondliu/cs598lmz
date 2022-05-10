import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap length is zero</code>.
I'm not sure how to fix this. I tried <code>m.close()</code> after truncating and then reopening the file, but that didn't help.
I'm using Python 3.4.3 on Windows.


A:

You can't use <code>mmap</code> in this way.  <code>mmap</code> is a memory-mapped file.  It creates a view of the file in memory.  If you truncate the file, the memory mapping is no longer valid.
You can use <code>mmap</code> to read a file, then truncate it, but you can't use the <code>mmap</code> object after truncating the file.

