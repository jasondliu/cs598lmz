import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'2'

with open('test', 'rb') as f:
    print(f.readline())
</code>
Prints out <code>b'2'</code> as expected, but when I open the file in vim, vim shows <code>^@</code> instead.
What is the reason for this? Is there any way to fix this?

