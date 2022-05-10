import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()

print(a)
</code>
I was expecting <code>a</code> to be an empty array: <code>[]</code>. However, I get <code>[1]</code>. Why is the mmap still retaining the old data after I truncate the file?
I'm using Python 3.4.1 on Windows 7.


A:

<code>truncate</code> doesn't automatically call <code>flush</code> (which would update the file with changes in memory). You need to manually call <code>flush</code> after truncating.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    f.flush()
    a = m[:]
    m.close()

print(a)  # prints b''
</code>

