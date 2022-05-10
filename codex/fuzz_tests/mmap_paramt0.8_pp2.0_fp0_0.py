import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1, access = mmap.ACCESS_WRITE)
    m[0] = 'a' # raises exception
    m.close()

with open('test', 'rb') as f:
    print(f.read())
</code>
On my computer this raises the exception:
<code>Traceback (most recent call last):
  File "C:/Users/russ_/OneDrive/Documents/Programming/python/test.py", line 6, in &lt;module&gt;
    m[0] = 'a'
ValueError: mmap slice assignment must be a single byte
</code>
It appears that in Python 2, strings are equivalent to bytes objects, which is why this works in Python 2. You could fix this by using <code>chr</code>:
<code>m[0] = chr(ord('a'))
</code>
Or, as Henry Yik pointed out, you could use <code>bytes</code>:
<code>m[0] = bytes([ord('a')])
</code>
Or, as @Gareth noted, you could just use a
