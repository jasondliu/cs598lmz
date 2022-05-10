import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
</code>
I get:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    m.resize(10)
mmap.error: [Errno 22] Invalid argument
</code>
While the following works on Windows:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(10)
</code>
Same problem with mmap.ALLOCATE.
What's the issue ?


A:

I figure it out finally.
On Linux, resize is limited by the size of the datablock on which the target resides, rather than the actual filesystem size.
See this link for more information.

