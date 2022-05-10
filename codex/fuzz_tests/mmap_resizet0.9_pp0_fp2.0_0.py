import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
print(a)
</code>
Output:
<code>[]
</code>
It seems that the file pointer is not updated immediately after the <code>truncate</code> call. Changing the file size and accessing the mmap object in the same place fixes the problem, as does blocking all access to the mmap object:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:]
    m.flush()
    f.truncate()
    m.flush()
    a = m[:]
    m.flush()

print(a)
</code>
Output:
<code>[]
</code>
I suspect that the mmap object has some internal cache that is not updated as expected, but it's hard to see an invariant that isn't satisfied here. Is there some kind of bug?
I tested this on Windows 10 with Python 3.6.4 and 3.7.
