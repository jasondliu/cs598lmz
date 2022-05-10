import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
It prints <code>b'\x00'</code> instead of <code>b'\x01'</code>.
Why? How to get the correct data?


A:

The <code>mmap</code> object is not updated when the file is truncated.
You can use <code>mmap.resize()</code> to update it:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(f.tell())
    a = m[:]
    print(a)
    m.close()
</code>

