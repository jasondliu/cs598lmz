import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
    m.close()
</code>
The above code prints <code>b'\x02'</code> which is expected.
However, if I change the code to:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
    m.close()
    f.seek(0)
    print(f.read(1))
</code>
The output is <code>b'\x02'</code> and <code>b'\x01'</code>.
Why is this? I thought the file and the mmap object would be in sync.


A:

From the mmap documentation:
<blockquote>
<
