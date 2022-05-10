import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.seek(0)
    m.write(bytes(2))
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
I would expect the output to be <code>b'\x02'</code> but instead I get <code>b'\x01'</code>.
I have also tried to use <code>mmap.ACCESS_WRITE</code> and <code>mmap.ACCESS_COPY</code> instead of <code>mmap.ACCESS_READ</code> but the result is the same.
What am I doing wrong?

