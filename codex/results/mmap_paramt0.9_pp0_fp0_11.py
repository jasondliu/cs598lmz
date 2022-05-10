import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, prot=mmap.PROT_READ)
</code>
But this fails with
<code>Traceback (most recent call last):
  File "&lt;stdin&gt;", line 2, in &lt;module&gt;
  File "/usr/lib/python3.5/mmap.py", line 256, in __init__
    access=access)
OSError: [Errno 22] Invalid argument
</code>
When I open the file in read/write mode and try to open a map in read/write mode, it works.
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, prot=mmap.PROT_WRITE|mmap.PROT_READ)
</code>
What is going on?


A:

You can see the error message via <code>strerror</code>:
<code>&gt;&gt;&gt; import mmap, os
&gt;&gt;&gt; os.strerror(22)
'Invalid argument
