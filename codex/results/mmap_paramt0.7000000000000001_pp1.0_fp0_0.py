import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m)
    print(m[0])
    m[0] = b'2'
</code>
The file is successfully created and the variable m is not None. However, the variable m contains only one number '1' and the variable m[0] is also equal to 1. I'm expecting the variable m to contain the whole file, not only the first character.
So, my question is: what am I doing wrong?


A:

That's because you are only writing a single byte in your binary file, <code>bytes(1)</code> only contains the byte value <code>1</code>. If you want to write multiple bytes, you need to pass a number to the <code>bytes</code> constructor.
Instead of
<code>f.write(bytes(1))
</code>
You need
<code>f.write(bytes(10))
</code>
or
<code>f.write(b'1' * 10)
</code>

