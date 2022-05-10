import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[0] = 0xFF
</code>
What is the easiest way to do the same thing in Python 3?
I tried the following but it doesn't work:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    m[0] = 0xFF
</code>


A:

Simply,
<code>m[0:1] = b'\xff'
</code>

<code>m[0] = 0xFF
</code>
doesn't work because in Python3, <code>m[0]</code> is <code>bytes</code> type, so it doesn't support byte assignment.
<code>m[0]</code> in Python2 is <code>str</code> type, which supports byte assignment.
<code>mmap</code> object in Python3 returns <code>bytes</code> object, in Python2, it returns <code>
