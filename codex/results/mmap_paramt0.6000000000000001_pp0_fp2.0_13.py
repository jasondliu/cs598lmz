import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = 49
    m.flush()
    m.close()

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read(1))
    m.close()
</code>
Output:
<code>b'0'
</code>
But if I change <code>m[0] = 49</code> to <code>m[0] = b'1'</code> then it works as expected. Am I doing something wrong here?


A:

Yes, you are doing something wrong.
The <code>__setitem__</code> method of the <code>mmap</code> object expects a byte string, not an integer. In Python 3, an integer can be converted to a byte string by <code>bytes([integer])</code>, but in Python 2, an integer is not a byte string, and the <code>__setitem__</code> method does not know how to convert it to one.
In Python 2, you need to change the <code>m
