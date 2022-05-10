import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
The last line raises <code>ValueError: mmap offset is greater than file size</code>.
But I thought that since I have opened the file with <code>r+b</code>, I have permission to read and write, and truncate the file.
What am I doing wrong?


A:

I think you are doing nothing wrong. It is just that <code>mmap</code> is not designed to work with truncated files.
From the documentation:
<blockquote>
<p>The mmap constructor creates a memory-map to an existing file. You must specify at least one of the following access flags: ACCESS_READ, ACCESS_WRITE, or ACCESS_COPY. If ACCESS_WRITE is specified, the file may not be larger than the system’s page size. If ACCESS_COPY is specified, the file may be any size.</p>
</blockquote>
If you want to truncate the file and still use <code>mmap</code>, you need to create a new <code>mmap</code> object after truncating the file.

