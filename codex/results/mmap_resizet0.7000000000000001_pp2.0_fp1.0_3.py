import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
# []
</code>
And this is the output I expected:
<code>b'\x01'
</code>
I know that truncating a file causes all data to be discarded but the file itself should be still open, right?
So is there an elegant way to achieve the expected behavior?


A:

Yes, you can use <code>mmap</code> to obtain a <code>bytes</code> object with the same data as the file (before truncation). Here's a working example:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    a = m[:]
    f.truncate()

print(a)
# b'\x01'
</code>

