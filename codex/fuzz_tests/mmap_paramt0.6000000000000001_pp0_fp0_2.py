import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[0] = b'0'
    m.close()
</code>
This works as expected, and writes a zero to the file. However, if you remove the <code>b</code> in the <code>f.write</code> line, the file is overwritten with a single byte of value 49.
I'm using Python 3.4.2. Does the <code>b</code> in the <code>f.write</code> line have any effect on the file, or is this a bug?


A:

This is a bug, but not in the Python interpreter.  The issue is that you are writing a single ASCII character to the file.  The ASCII code for the character '1' is <code>49</code>.  When you write a single character, you are actually writing a byte, which is why you see the value <code>49</code> in the file.  However, when you write the byte <code>49</code> to the file, you are actually writing a byte that represents the ASCII character '1'.  In the world of Python, there is no difference between the character '1'
