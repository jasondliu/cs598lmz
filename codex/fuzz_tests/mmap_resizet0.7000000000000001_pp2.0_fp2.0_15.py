import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    m.close()
</code>
Output:
<code>b'\x00'
</code>
Somehow the truncate call is not reflected in the mmap object. It is like the buffer is cached by the mmap object. 
I know the method could be dangerous, but is there a clean way to do it?
EDIT
I just found out that if I use mmap to truncate, it works.
<code>import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m.resize(0)
    a = m[:]
    print(a)
    m.close()
</code>
Output:
<code>b''
</code>
However, I would still like to know if there is a way for <code>f.truncate()</code> to work.


A:

As @user2357112 noted, you are not
