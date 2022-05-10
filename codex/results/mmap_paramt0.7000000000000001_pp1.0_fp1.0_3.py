import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = ord('s')
</code>
You can't just write a string to a memory mapped file, you need to write the bytes that make up that string, so I've added <code>ord()</code> to convert the <code>'s'</code> to its numerical value (that's what <code>ord()</code> does).
You can then read the file back to see the changes:
<code>with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m.read())
</code>
and you'll see:
<code>b's'
</code>
The <code>b</code> prefix on the string indicates that these are bytes, not a unicode string.

