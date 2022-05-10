import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot mmap an empty file
</code>
I think this is because the file is being truncated before the <code>m[:]</code> is called.
I'm wondering if there is a way to get around this?


A:

You can't use <code>mmap</code> on an empty file.
<blockquote>
<p>The mmap() function requires a file descriptor fd referring to an open file. The file must be opened with read permission, even if mmap() will only be used for writing. If the file is opened for update (i.e., both read and write), the file may not actually be updated until msync() or munmap() is called.</p>
</blockquote>
If you want to map an empty file, you can create a temporary file with <code>tempfile.NamedTemporaryFile</code>, and then <
