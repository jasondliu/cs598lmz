import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    for b in m:
        print(ord(b))
</code>
I got 48. Why? The byte(1) seems to be converted to "0". 


A:

You need to turn <code>1</code> into a byte string containing the character with code <code>1</code>.  Change your bytes call to:
<code>f.write(bytes([1]))
</code>
There are 2 problems with your current code.

You are passing an integer to <code>bytes</code>, which is not allowed.
<code>bytes(1)</code> evaluates to <code>b'\x00'</code> which is the byte string containing
the byte with code <code>0</code>.

I'm not sure why the first problem is not triggering an exception.

