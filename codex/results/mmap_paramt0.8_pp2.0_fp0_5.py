import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    m[0] = 1
    m.close()
</code>
This gives the following error:
<code>m[0] = 1
TypeError: a bytes-like object is required, not 'int'
</code>


A:

This is because in Python 3, every <code>bytes</code> object has <code>__setitem__</code> set to a method that requires an <code>int</code> to be passed as the first argument to it. It's not actually the same type as the <code>mmap</code> object!
You need to treat the <code>bytes</code> object as a series of individual bytes, and you can't do that by using its <code>__setitem__</code> method; you have to <code>bytes.__getitem__</code> on it and then convert the result to an <code>int</code>:
<code>m.__setitem__(0, ord(m.__getitem__(0)))
</code>
Of course, this is a little silly, so
