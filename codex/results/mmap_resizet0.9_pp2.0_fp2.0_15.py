import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
</code>
gives error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    a = m[:]
ValueError: negative seek position
</code>
It fails because <code>mmap</code> doesn't track if its file got truncated and still thinks that it represents an mmap on file with 1 byte.
If you however modify the <code>m[:]</code> to raw byte address like <code>m[0]</code>, then it will work.
<code>a = m[0]
</code>
Therefore I believe it is a bug, since negative seek is a plain wrong thing to do. 

