import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    b = m[::-1]
    c = m[::-2]
    d = m[::2]
    print(a)
    print(b)
    print(c)
    print(d)
</code>
This code returns:
<code>b'\x01'
b'\x01'
b''
b'\x01'
</code>
Changing the reverse step to 3, i get:
<code>b'\x01'
b''
b''
b''
</code>
I would expect:
<code>b'\x01'
b''
b''
b'\x01'
</code>
Why is this? According to python docs, mmap should be able to access data beyond the end of the file. Also, it seems that not only does mmap not find any data beyond the end of the file, but it also does not update the mapping even after i've truncated the original file (which is still open).
I've also tried this in python 3.4, but there are some subtle differences in behavior and it seems to be a bit inconsistent
