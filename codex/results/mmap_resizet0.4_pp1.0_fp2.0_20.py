import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect <code>a</code> to be an empty byte array, but it's not. It's <code>b'\x01'</code>.
How can I get an empty byte array?


A:

You are using the <code>mmap</code> object after you truncated the file.
The <code>mmap</code> object is not automatically updated when you truncate the file.
You can use <code>mmap.resize</code> to resize the <code>mmap</code> object.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]
</code>

