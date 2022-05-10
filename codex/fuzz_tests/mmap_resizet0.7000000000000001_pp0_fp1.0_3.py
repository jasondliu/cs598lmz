import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
</code>
The output is <code>b''</code>, but I expected <code>b'\x00'</code> as the byte is not removed from memory.
Question:
Is there a way to get <code>b'\x00'</code> as output?
Note: The question is similar to this one, but the answer suggested there, doesn't work with truncate.

