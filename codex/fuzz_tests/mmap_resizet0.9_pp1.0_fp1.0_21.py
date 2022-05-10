import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Output:
<code>mmap.error: [Errno 12] Cannot allocate memory
</code>
Is this bug? or designed beavior?


A:

It's due to bug. When process use enormous amount of virtual memory, it's usually causes this error.

