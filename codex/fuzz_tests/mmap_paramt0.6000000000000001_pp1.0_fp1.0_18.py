import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    assert m.read_byte() == 2
</code>
I would have expected the assert to fail, since I opened the file with <code>'wb'</code> mode, but apparently <code>mmap</code> will also write to the file. Is this documented somewhere?


A:

The <code>mmap</code> module's documentation says:
<blockquote>
<p>mmap(fileno, length[, flags[, prot[, access[, offset]]]])<br/>
  Create a new memory-mapped file object. The argument <em>fileno</em> must be an open file descriptor (as returned by os.open()) <strong>which will be closed when the mmap is closed</strong>, so don’t close it explicitly.</p>
</blockquote>
(emphasis mine)
So this is documented.

