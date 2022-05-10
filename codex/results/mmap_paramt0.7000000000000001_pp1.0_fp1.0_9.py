import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0) # 0 means to map the whole file
    m.resize(10)
    print(m[:])
    m.write(bytes(9))
    print(m[:])
</code>
Output:
<code>b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
</code>
So, it looks like I'm able to write to the mapped memory, but the underlying file isn't being updated. Is this the expected behavior?
Thanks!


A:

There are two problems here. 
First, you are not flushing the file after writing.
Second, you are not closing the map before writing.
Try this:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mm
