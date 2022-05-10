import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
I expect the variable <code>a</code> to be an empty byte array, but it is not.
How can I get the expected behavior?


A:

The problem is that you are trying to read from a <code>mmap</code> object that is not valid anymore.
The <code>mmap</code> object is not valid anymore because you truncated the file.
You can truncate the file and then resize the <code>mmap</code> object.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    m.resize(0)
    a = m[:]

print(a)
</code>

