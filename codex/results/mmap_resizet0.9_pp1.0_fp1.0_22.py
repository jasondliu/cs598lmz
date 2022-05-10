import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Here I expect <code>a</code> would be empty, but it's <code>b'\x01'</code>.
What is the expected behaviour here? Thank you in advance!


A:

It is expected behavior. Section "16.6.2.2 Modifying a mmap" in the docs:
<blockquote>
<p>How, when and whether file content is updated depends on the parameters to <code>&lt;code&gt;mmap()&lt;/code&gt;</code> and your operating system.</p>
<p>When modifications are made to a memory-mapped file, it is implementation dependent when the changes are actually written out to the underlying file. There are some methods provided in the mmap module which can be used to force updated data to be written to disk. On Unix and macOS, changes to the
  memory-mapped array are made visible to other processes mapping the same file by calling msync() with the MS_SYNC flag, or by simply closing the file descriptor associated with the memory-mapped file.</p>
<p>Note On Windows, use flush() instead of
