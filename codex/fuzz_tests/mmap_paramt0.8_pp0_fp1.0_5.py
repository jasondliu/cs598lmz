import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)

print(m[:])
</code>
This generates the following error:
<code>mmap.error: [Errno 12] Cannot allocate memory
</code>
What is the issue and how can it be fixed?

