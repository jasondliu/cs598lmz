import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'a'
    print(m[0])
</code>
The output is <code>b'a'</code> which is expected.
If you want to write a string (which is a sequence of characters), you can use <code>ord</code> to get the character code, and <code>chr</code> to get the character from the character code.
<code>with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('a')
    print(chr(m[0]))
</code>
The output is <code>'a'</code>.

