import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 1
    m.close()
</code>
But it doesn't work.
Any ideas?


A:

The <code>mmap</code> module is not the right tool for this.  It works on existing files and requires that the file be opened in read/write mode.  It does not create new files.
From the documentation:
<blockquote>
<p>The mmap constructor is used to create a memory-mapped file. It takes a file descriptor fd
  and an optional length size, and uses them to create a memory-mapped file object. The file
  descriptor fd must refer to an open file, but must not be opened with access mode os.O_RDONLY.
  The optional length size is the initial size of the mapped region. If size is omitted, the
  size of the file is used.</p>
</blockquote>
If you want to create a new file and write to it, use the <code>os.open()</code> function to open a file descriptor for the new file and then use <code>os.write()</code> to
