import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I get the error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: cannot read from closed file
</code>
The documentation says:
<blockquote>
<p>mmap.mmap(fileno, length[, flags[, prot[, access[, offset]]]])</p>
<p>...</p>
<p>fileno
      This is the file descriptor of the file to be mapped. The file descriptor must be opened in read-write mode. The file descriptor will not be closed by the mmap constructor. The file descriptor is inherited by child processes created by os.fork() and is closed by the operating system when the process exits.</p>
</blockquote>
So I would expect that the file descriptor remains open after the <code>truncate()</code> call.
What am I doing wrong?


A:

You can't truncate a file that is memory mapped.  It's an OS limitation.  See the docs for <code>trunc
