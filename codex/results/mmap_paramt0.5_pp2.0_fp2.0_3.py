import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'\x00'
</code>
I am trying to change the first byte of the file to be <code>0</code>. However, the file is not changed.
When I do <code>m[0] = b'\x01'</code> it does change the file, but not to <code>0</code>.
Why does this happen?


A:

Your code works as expected.
I've modified it to print the value of the first byte before and after the <code>m[0] = b'\x00'</code> assignment:
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = b'\x00'
    print(m[0])
</code>
Output:
<code>b'\x01'
b'\x00'
</
