import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]

print(a)
</code>
This results in <code>b''</code>, but I would expect <code>b'\x01'</code>.
I would also expect <code>m[:]</code> to raise an exception, but it does not.
Why does this happen? Is it the expected behaviour?


A:

<code>mmap.mmap</code> reads the file into the buffer and the file remains untouched until you modify the buffer.
But when you call <code>f.truncate()</code>, the file content is truncated immediately, and that's why you get an empty <code>bytes</code> object when you read the file.

