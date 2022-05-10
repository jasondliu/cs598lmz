import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This raises an error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
Is there a way to get rid of this error?


A:

The documentation is pretty clear here:
<blockquote>
<p>If <code>&lt;code&gt;length&lt;/code&gt;</code> is <code>&lt;code&gt;0&lt;/code&gt;</code>, the maximum length of the map will be the current size of the file when <code>&lt;code&gt;mmap&lt;/code&gt;</code> is called. <strong>Files created using the <code>&lt;code&gt;mmap&lt;/code&gt;</code> module do not grow like regular files. To enlarge the file, the process must have write permission on the filesystem containing the file, and must open the file with <code>&lt;code&
