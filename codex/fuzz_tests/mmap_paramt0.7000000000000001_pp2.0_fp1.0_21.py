import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[1]
</code>
I would expect this to not access the second byte, so that I can access it later. But instead, I get the following exception:
<code>  File "h.py", line 8, in &lt;module&gt;
    m[1]
mmap.error: [Errno 5] Input/output error
</code>
I am trying to create a file with some metadata on the first bytes and the rest of the file is data that I want to access in a random fashion.
Note that I am not asking for the reason for the exception, just for a way to achieve my goal.


A:

A <code>mmap</code> object cannot be used to access a file that you have opened for writing. You need to <code>open</code> the file in read-only mode, and then use <code>mmap</code> to open it for writing.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap
