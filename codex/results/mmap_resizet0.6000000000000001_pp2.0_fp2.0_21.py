import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I'm getting the error: <code>OSError: [Errno 22] Invalid argument</code>.
The code works if I don't use <code>mmap</code>.


A:

You can't use <code>mmap</code> after truncating the file.
The documentation says:
<blockquote>
<p>If the file is resized, any offsets beyond the current size of the file are no longer valid. </p>
</blockquote>
(The file is resized by the <code>truncate()</code> call.)

