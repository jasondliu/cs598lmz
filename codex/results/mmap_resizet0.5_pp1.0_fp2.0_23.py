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
I get the following error:
<code>Traceback (most recent call last):
  File "./test.py", line 11, in &lt;module&gt;
    a = m[:]
ValueError: mmap offset is greater than file size
</code>
I understand that this is because the file is empty, but I would like to know if there is a way to do this without closing the file descriptor and reopening it.
Thanks


A:

No, there is no way to do this without closing and reopening the file.  Python's mmap module is implemented in C, and the underlying OS calls that it uses to create and manipulate memory maps are not compatible with the OS calls that are used to truncate a file.  If you want to truncate a file that is open for writing, you need to close the file first, truncate it, and then reopen it.

