import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[0])
    m[0] = 1
    print(m[0])
    m[0] = 99
    print(m[0])
    m[0] = 128
</code>
Output:
<code>1
1
99
Traceback (most recent call last):
  File "test.py", line 13, in &lt;module&gt;
    m[0] = 128
ValueError: byte must be in range(0, 256)
</code>
(I'm using Python 3.6, but I get the same error on 2.7.)
I don't understand why it's not possible to assign 128 to <code>m[0]</code>. I know that, in Python, bytes are signed integers between -128 and 127, but I don't see why the same should apply to <code>mmap</code> objects.
Is there a way to write an arbitrary byte (0-255) to a <code>mmap</code> object?


A:

<code>m[0] = 128</code> is equivalent to <code>m
