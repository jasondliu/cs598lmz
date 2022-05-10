import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
output of the code above: <code>[220]</code>
What is the logic behind this error?


A:

The documentation is not clear on what happens when you try to open an mmap with a file that is truncated before the mmap was created.
The correct behavior is that the mmap stays valid, but the old content of the file is no longer accessible.
You can easily verify this by creating the mmap first, then open the file in write mode, and truncate it.
The only way the mmap would be invalid is if the file was truncated to 0 bytes. If you do that, you must close and reopen the mmap.

