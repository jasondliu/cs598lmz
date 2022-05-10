import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
    m.close()
</code>
I have tried to use <code>mmap.ACCESS_WRITE</code> but it doesn't work.
I have also tried to use <code>m[0] = b'\x00'</code> and <code>m[0] = 0</code> but it doesn't work.
I have also tried to use <code>m.write(b'\x00')</code> but it doesn't work.
I have also tried to use <code>m.write(0)</code> but it doesn't work.
I have also tried to use <code>m.write(bytes(1))</code> but it doesn't work.
I have also tried to use <code>m.write(bytes(1)[0])</code> but it doesn't work.
I have also tried to use <code>m.write(bytes(1)[0:1])</code> but it doesn't work.
I have also tried to use <code>m.write(bytes(1)[0:2])
