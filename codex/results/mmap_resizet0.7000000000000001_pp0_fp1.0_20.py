import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # &lt;-- Line 35
</code>
The following error occurs when I run the above code:
<code>Traceback (most recent call last):
  File "test.py", line 35, in &lt;module&gt;
    a = m[:]
OSError: [Errno 9] Bad file descriptor
</code>
I'm pretty sure that the file descriptor is valid, so why does the error occur?


A:

The docs for <code>mmap.mmap</code> state:
<blockquote>
<p>The underlying file descriptor of the file object fd must be valid; it will not be closed.</p>
</blockquote>
You're trying to use a file descriptor that is created by <code>open</code> with the <code>'r+b'</code> flag, which is documented to be:
<blockquote>
<p>Open for reading and writing. The stream is positioned at the beginning of the file.</p>
</blockquote>
Since "positioning the stream" requires the file descriptor to be valid, the file descriptor is no longer valid after you
