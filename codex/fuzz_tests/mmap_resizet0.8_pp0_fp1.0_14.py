import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
Any idea?


A:

<code>mmap</code> uses the OS's page cache, which means that the underlying file - e.g. the  <code>test</code> file you're opening - must be opened.
<code>truncate()</code> doesn't open the file, it merely truncates it (by clearing the FS's inode). However, it still tries doing the actual truncation via the OS's page cache. This is why it fails with <code>ENOENT</code> - the page is not present in the page cache.
If you want the data to go away, you'd need to <code>open()</code> the file (e.g. via <code>f</code> again).

