import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])
</code>
This is throwing an exception 
<code>Traceback (most recent call last):
  File "m.py", line 8, in &lt;module&gt;
    print(m[:])
ValueError: memory mapped string must begin at a length-aligned address
</code>
Can you please explain the reason for this error?
Also how do I get the contents of the file using map?
The code works fine for a file with size greater than 1 byte.


A:

Why does this matter? There's no need to seek around like that. Just do:
<code>with open("test", "rb") as f:
    print(f.read())
</code>
If you really want to use <code>mmap</code>, you can do
<code>with open("test", "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    print(mm.read())
</code>
But the real question is
<blockquote>
<p>why are you using <code
