import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b'\x00')
    m.seek(0)
    m.write(b'\x01')
    m.flush()
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
The output is <code>b'\x00'</code> instead of <code>b'\x01'</code>.
I am using Python 3.6.2 on Windows 10.
What am I doing wrong?


A:

You need to <code>seek</code> to the start of the file before writing to it.
<code>m.seek(0)
m.write(b'\x01')
</code>

