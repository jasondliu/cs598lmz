import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)

print(len(a))
</code>
Output:
<code>b''
0
</code>
I would expect an exception since the file is truncated but the memory map is still there.
<code>OSError: [Errno 9] Bad file descriptor
</code>

