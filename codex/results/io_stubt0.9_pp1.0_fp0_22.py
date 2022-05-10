import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
</code>
I'll not take responsibility for the consequences of using such a module: it's just a demonstration.  If you really want a <code>io.BufferedReader</code>, you'll have to implement <code>read</code> or <code>read1</code> as well (well, <code>read1</code> isn't necessary, as it's a read-only class and only overrides <code>__init__</code>, <code>flush</code>, and <code>detach</code> methods).  If you only do a small amount of writes, then <code>-1</code> might suffice for those methods and you wouldn't have to implement them at all.  If you truly want a raw byte view an object, then you wouldn't write any methods on the <code>io.RawIOBase</code> derived class at all.  It's all up to you.

