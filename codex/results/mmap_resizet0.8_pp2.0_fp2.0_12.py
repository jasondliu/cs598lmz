import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
</code>
I'm getting the error as follows:
<code>Traceback (most recent call last):
  File "/usr/lib/python3.4/mmap.py", line 538, in __enter__
    self.__fd = fd = _os.open(filename, access)
FileNotFoundError: [Errno 2] No such file or directory: 'test'</code>
I'm unable to understand why is this error getting triggered when I'm able to successfully mmap the file before truncating it.
I've tried googling it but didn't find anything relevant to my problem.
Any help would be appreciated, thanks.


A:

The problem is that you are truncating the file before calling <code>mmap.mmap</code>.
The following code:
<code>with open('test', 'r+b') as f:
    f.truncate()
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    m.close()
</code>
is equivalent to:
<code
