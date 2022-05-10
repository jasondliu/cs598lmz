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
In this case, a is an empty string, which would be expected if the file were truncated first and then the mmap was read. However, if the mmap is read first and then the file is truncated, a is a single byte.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    a = m[:]
    f.truncate()
    m.close()

print(a)
</code>
What is happening here? Are there any guarantees about the order in which these operations will be performed?


A:

The answer is that you can't really rely on the order of operations when using a mmap object. The mmap object provides a view of the file's contents, not the file itself. So the ordering of operations between the mmap object and the file object are undefined.
One way to achieve the result you want is to
