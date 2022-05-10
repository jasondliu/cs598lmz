import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
I can't see why this is happening. The file is opened with <code>r+b</code> so the file should be readable and writable. The <code>mmap</code> is created with the file descriptor, so it should be valid. The <code>truncate</code> call should have no effect on the <code>mmap</code> object.
I'm using Python 3.5.2 on Windows 10.


A:

You are truncating the file to 0 bytes, so the <code>mmap</code> object is no longer valid.
From the <code>mmap</code> documentation:
<blockquote>
<p>The <code>&lt;code&gt;mmap()&lt;/code&gt;</code> function creates a new mapping in the virtual address space of the calling process. The starting address for the new mapping is specified in <em>addr</em>. The length argument specifies the length of the mapping.</p>
<p>The <em>flags</
