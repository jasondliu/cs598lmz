import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m.write(bytes(1))
    m.close()
</code>
I'm getting:
<code>Traceback (most recent call last):
File "C:/Users/user/PycharmProjects/parser/test.py", line 9, in &lt;module&gt;
    m.write(bytes(1))
ValueError: must be readonly or copy-on-write mmap
</code>
While this works:
<code>m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ|mmap.ACCESS_WRITE)
</code>
I also tried using <code>mmap.ACCESS_WRITE</code> on file opened in <code>'a'</code> mode, or <code>'w'</code> mode, or both <code>'w+'</code> mode, but all with the same result.
I tried it on two computers, with python 2.7.10 and 3.4.3, same result.
Is it a
