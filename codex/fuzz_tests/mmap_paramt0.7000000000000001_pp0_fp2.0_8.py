import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.flush()

with open('test', 'rb') as f:
    print(f.read())
</code>
I get this output:
<code>b'\x01'
</code>
I expected to see:
<code>b'\x02'
</code>
But the file content remains the same.
I then try another method:
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(1)
    m.write(bytes(2))
    m.flush()

with open('test', 'rb') as f:
    print(f.read())
</code>
This time I get the result I want:
<code>b'\x01\x02'
</code>
I didn't expect the seek to be necessary. Is this the normal behavior of MMAP?


A:
