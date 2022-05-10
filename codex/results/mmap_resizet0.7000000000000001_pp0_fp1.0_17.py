import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
If I run the code above, I get:
<code>Traceback (most recent call last):
  File "C:/Users/XXXX/Desktop/test.py", line 9, in &lt;module&gt;
    a = m[:]
ValueError: mmap slice assignment is larger than available data
</code>
Why does it happen? I thought it would return an empty bytestring or something.

