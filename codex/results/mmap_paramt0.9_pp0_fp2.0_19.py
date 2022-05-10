import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(1)  # &lt;---- Error!
</code>
The error I get is:
<code>mmap.error: cannot resize a read-only memory map
</code>
I expected to be able to use <code>mmap</code> with a writable file with standard C fopen modes, yet for the life of me I can't seem to get it right. Is Python's <code>mmap</code> broken?


A:

Opening the file with something like <code>mmap.PROT_READ | mmap.PROT_WRITE</code> solved my problem.

