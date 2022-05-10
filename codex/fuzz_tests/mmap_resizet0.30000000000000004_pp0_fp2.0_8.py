import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is:
<code>b'\x01'
</code>
I was expecting that the output would be <code>b''</code>.
Why is the output not <code>b''</code>?


A:

The <code>mmap</code> object is not updated when you truncate the file.  You can see this by printing the size of the <code>mmap</code> object:
<code>print(m.size())
</code>
This will print <code>1</code> even after you've truncated the file.

