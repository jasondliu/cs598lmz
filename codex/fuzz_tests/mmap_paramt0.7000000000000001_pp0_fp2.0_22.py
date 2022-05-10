import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
The file does not get modified.
What am I doing wrong?


A:

The problem is that you are opening the file with <code>wb</code> which prevents any of the data from being read.
If you just open it with <code>r+b</code> it seems to work fine:
<code>with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'

with open('test', 'rb') as f:
    print(f.read())
</code>
Output:
<code>b'\x00'
</code>

