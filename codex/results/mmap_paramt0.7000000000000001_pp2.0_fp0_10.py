import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 48
    m.close()

with open('test', 'r') as f:
    print(f.read())
</code>


A:

Python 2 <code>bytes</code> is a <code>str</code> type so you are writing a <code>str</code> to a file. With Python 2, you should use <code>bytearray</code> instead.

