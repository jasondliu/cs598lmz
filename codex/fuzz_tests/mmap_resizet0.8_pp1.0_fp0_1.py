import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:] # error

    m = mmap.mmap(f.fileno(), 0)
    m.resize(10000000000000000000)
</code>
I get an error
<code>mmap.error: [Errno 22] Invalid argument
</code>
How can I remove this error? I need to resize <code>mmap</code> if file size is changed.


A:

Use <code>mmap.resize()</code> to change the size of an existing memory-mapped file object, before or after <code>truncate()</code>ing the underlying file.
The following script demonstrates the use of <code>mmap.resize()</code> to <code>truncate()</code> a file and resize the memory-mapped region to match:
<code>import mmap
with open('test', 'ab') as f:
    m = mmap.mmap(f.fileno(), 0)
    print("Before:", m.size())
    f.truncate(42)
    m.resize(42)
    print("After :", m.
