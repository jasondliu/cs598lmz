import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]  # ok
    m[:] = a  # no exception, but silently fail
    m.close()
    del m

    m = mmap.mmap(f.fileno(), 0)
    m.write(bytes(1))  # ok
    m.close()
</code>
Is there any way to detect whether the original mapping is still alive or not?


A:

Note that <code>m[:] = a</code> does not raises <code>ValueError</code>, but <code>OverflowError</code>.

Another method is to create your own class and handle the error.
<code>class MyError(Exception):
    pass

class MyBuffer(mmap.mmap):
    def __setitem__(self, key, value):
        try:
            super().__setitem__(key, value)
        except OverflowError:
            raise MyError

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = MyBuffer(f.fil
