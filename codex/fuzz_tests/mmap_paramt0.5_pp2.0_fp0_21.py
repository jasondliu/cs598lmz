import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
</code>
It will print 2 as expected. But if I change the first line to
<code>with open('test', 'wb', buffering=0) as f:
</code>
it will print 1, which is not what I expected.
I thought <code>buffering=0</code> means no buffering, so the write operation should be performed immediately. Why does it still print 1?


A:

This is because the <code>mmap</code> module uses the <code>os.open()</code> function to open the file, which doesn't support the <code>buffering</code> argument.
You can see this in the source code:
<code>def _mmap_open_osfhandle(fd, flags):
    """Open an mmap'ed file from an OS handle"""
    # XXX This function is only used on Windows
    # XXX The flags parameter is not used
    # XXX The fd parameter is an integer
    # On Windows, open
