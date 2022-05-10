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
But I get error:
<code>Traceback (most recent call last):
  File "test.py", line 8, in &lt;module&gt;
    f.truncate()
TypeError: integer argument expected, got float
</code>
Could you tell me why <code>truncate</code> doesn't want to be used with <code>memory map</code>? What can I use instead of truncate in this case?

