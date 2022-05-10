import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
As far as I know, Windows implementation of memory mapped files are different from Unixes and there is nothing equivalent to file descriptors. I want to use it to move around the file.
Edit: For reference, in Unix, the expected behavior would be for <code>m[:]</code> to raise <code>ValueError: cannot extend memory mapping beyond the end of file</code>.


A:

You're getting a <code>ValueError</code>.
<code>try:
    m[:]
except ValueError as e:
    print(e)
</code>
Output:
<code>cannot extend memory mapping beyond the end of file
</code>
And that's what it should do when fileno is not valid.
I can't find where the documentation says it. It certainly doesn't say it returns None.
The <code>BufferedIOBase</code> documentation has a minimal description of what might happen.
<blockquote>
<p>Implementations may raise UnsupportedOperation if they do not support the operation (for example, attempting to use a buffered I/O implementation to read from a socket object).
