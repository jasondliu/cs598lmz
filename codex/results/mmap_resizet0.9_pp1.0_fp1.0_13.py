import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    m.close()
    print(a)
</code>
this give error
<code>Traceback (most recent call last):
  File ".\test.py", line 10, in &lt;module&gt;
    a = m[:]
BufferError: Existing exports of data: object cannot be re-sized
</code>
if i insert dummy line <code>print(a)</code> before <code>m[:]</code>, it works fine. like this
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[0]
    print(a)
    a = m[:]
    m.close()
    print(a)
</code>
What's wrong here?
I am following the doc
https://docs.python.org/2/library/mmap.html

