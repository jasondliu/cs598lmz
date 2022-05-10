import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The print statement prints <code>b'\x01'</code> as expected.
Now, if I change the last line to <code>print(m[:])</code>, I get a <code>ValueError</code> saying <code>mmap slice length cannot be negative</code>.
If I change the last line to <code>print(m[1:])</code>, I get <code>b''</code> as expected.
I don't understand why the first case causes a <code>ValueError</code>. 

