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
I would expect the output to be <code>b'\x02'</code>, but it is <code>b'\x01'</code>.
Why is this?


A:

You are opening the file in <code>wb</code> mode, which truncates the file.
You need to open the file in <code>r+b</code> mode to avoid truncation:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(2))
    m.seek(0)
    print(m.read(1))
    m.close()
</code>

