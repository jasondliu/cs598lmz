import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
For some reason, the last line fails with:
<code>mmap.error: [Errno 22] Invalid argument
</code>
Any idea, why this fails and how to fix it?
EDIT: The solution must work on Windows as well. So, I don't think I can use <code>posix_fallocate</code> on Windows.


A:

Here is the code I ended up with. Please let me know if you find any issues.
<code>import mmap
import os

def preallocate(file, size):
    """Preallocate disk space for a file.

    Raises an exception if the file already exists.
    """

    with open(file, 'wb') as f:
        f.truncate(size)

def extend(file, size):
    """Extend an existing file to a specified size.

    The file is filled with zeros if it is extended.

    Raises an exception if the file does not exist.
    """

    with open(file, 'r+b') as f:
        stat = os.fstat(
