import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
This code raises an exception:
<code>mmap.error: [Errno 22] Invalid argument
</code>
Is there a way to truncate a file which is mmapped?


A:

You can't.
The <code>mmap</code> module has a <code>resize()</code> method, but it only works if the file is opened with <code>MAP_SHARED</code> and the operating system supports it.
The documentation says:
<blockquote>
<p>If the file is opened for writing, this method may increase the file size. If the file is extended, the contents of the new area are undefined. The file’s size is not changed by this method if it is decreased.</p>
<p>On Windows, if the file is opened for writing, the file size can only be increased.</p>
</blockquote>

