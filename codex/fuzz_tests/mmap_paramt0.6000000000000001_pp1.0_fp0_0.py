import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    m.write(bytes(2))
    m.flush()
    m.close()

with open('test', 'rb') as f:
    print(f.read(1))
</code>
The problem is that the output is <code>b'\x01'</code> and then <code>b'\x01'</code>, instead of <code>b'\x01'</code> and then <code>b'\x02'</code>.
So the question is how to use <code>mmap</code> to write to a file at an arbitrary position?


A:

<code>mmap()</code> does not allow you to seek to arbitrary offsets, nor does it allow you to write to offsets beyond the end of the file. It is a memory-mapped file object, which allows you to access the file as a memory buffer, but it is not a file object.
If you have to write to the file at a particular offset, you need to seek to that offset and then write, or use the <code>writelines()</code
