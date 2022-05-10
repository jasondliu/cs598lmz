import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = b'0' * 65 * 1024 * 1024 * 1024
</code>
However, the output I get is:
<code>Traceback (most recent call last):
  File "C:\mmaptest.py", line 12, in &lt;module&gt;
    m[:] = b'0' * 65 * 1024 * 1024 * 1024
ValueError: mmap length is greater than file size
</code>
I would like to extend the file to 65 GB, instead of replacing whatever is already in the file.
I have already tried padding the file with blank data so that its size matches the size I want but it hasn't solved the problem.


A:

I can't duplicate the error.  If the error is not that the process runs out of memory (which is not typical on a 64-bit machine), then it would appear that <code>mmap</code> is unable to handle a file that has a growing logical end-of-file as it is being mapped.  It seems as if it always checks the current size of the file as it is opened before committing to do anything.  To work around this,
