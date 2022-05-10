import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))

with open('test', 'rb') as f:
    print(f.read(1))
</code>
Output:
<code>b'\x02'
b'\x02'
</code>
The file is updated!
The same code but with <code>'w+b'</code>:
<code>with open('test', 'w+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))

with open('test', 'rb') as f:
    print(f.read(1))
</code>
Output:
<code>b'\x02'
b''
</code>
The file is not updated!
Is there a way to update files with <code>mmap</code> when they are opened with <code>'w+b'</code>?



