import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(2)
</code>
<code>test</code> file is created with two bytes with value <code>2</code>.


A:

I think the problem is that you're using a Python 3.3 <code>bytes</code> object to set the <code>mmap</code> object, and <code>mmap</code> objects don't support that; they only support Python 2 <code>str</code> objects.
If you change your code to use <code>str</code> instead of <code>bytes</code>, it works:
<code>with open('test', 'wb') as f:
    f.write(str(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = str(2)
</code>
in Python 2, and:
<code>with open('test', 'wb') as f:
    f.write(bytes([1]))

with open('test', 'r+b') as f:

