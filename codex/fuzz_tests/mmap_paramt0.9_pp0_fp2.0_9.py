import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0:1] = bytes([255])
    m.flush()
</code>
gives me the <code>PermissionError: [Errno 13] Permission denied: 'test'</code>.
So, <code>mmap.mmap</code> needs a file opened for r/w or r+b access.
The docs don't tell me if this is actually necessary.
Does it matter if it is not opened for write access?

EDIT:
Actually, I don't need this right now. I was just curious.
I was forced to use <code>mmap.mmap</code> because I had an issue with the <code>mmap</code> binary mode on windows and python3.5.
<code>&gt;&gt;&gt; import mmap
&gt;&gt;&gt; with open('test', 'wb') as f:
...     f.write(bytes(1))
...
&gt;&gt;&gt; with open('test', 'rb+') as f:  # You have to use the rb+ mode on py35.
