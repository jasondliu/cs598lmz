import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
Why <code>a</code> is still 1 but not 0 (the empty bytes) as I want if <code>f</code> has been truncated? Is there any way to make <code>m</code> reflect the change of <code>f</code> after <code>truncate()</code>?


A:

Python's implementation copies the file data into its own buffers when mapping the file. That buffer is what you see.
You cannot use the <code>mmap</code> to truncate the file; this makes little sense in the first place, as you'd be truncating the file data that you already mapped, which would leave you with a stranded mmap object.
Simply close the mmap first:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.close()
    f.truncate(0)
</code>
or truncate by writing to the <code>mmap
