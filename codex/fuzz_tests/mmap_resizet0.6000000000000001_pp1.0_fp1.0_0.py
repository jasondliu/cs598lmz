import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
This is the error I get:
<code>print(a)
mmap.error: [Errno 22] Invalid argument
</code>
I would like to see the value <code>b'\x00'</code> printed.
Why does this happen, and how can I do it correctly?


A:

<code>mmap</code> is a wrapper around the <code>mmap()</code> system call.  The semantics of the system call are described in the <code>mmap(2)</code> man page.  The <code>MAP_FIXED</code> flag is not set, so the address at which the mapping is created is taken from the <code>mmap</code> object itself, which is the result of a call to the C function <code>PyLong_AsLong()</code>.  If the object is not an integer, or is out of range, then <code>PyLong_AsLong()</code> raises a <code>TypeError</code> exception.  But the Python interpreter does not see the error because the call to <code>
