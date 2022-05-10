import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    print(m[1]) # returns 0 (the byte value)
    print(m[2]) # returns 0 (the byte value)
</code>
I have 2 questions:

Why does a read from an invalid index return 0?
How do I detect the end of the <code>mmap</code>?



A:

In the C API, <code>mmap</code> returns <code>MAP_FAILED</code> on error.  This is a NULL pointer, and in Python 3, it's converted to <code>None</code>.  So you should check for that using <code>m is not None</code>.
You can also look at the return value of <code>mmap.mmap</code> (which is the same as <code>m</code>) to see if it's <code>None</code>.
If you're not getting <code>None</code> back when you call <code>mmap.mmap</code>, then the problem is that your platform doesn't support mmap.  This function is not available on Windows.

