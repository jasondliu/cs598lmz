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
view[0] = 0
</code>
This is valid code, but is not a good idea for various reasons. (CPython 3.9+ only protects <code>list</code> - it's possible to do this with typed memoryviews in earlier versions.)
The same goes for code that assigns to an element of a list while an iterator is in progress:
<code>some_list = [0, 1, 2, 3]
it = iter(some_list)
print(next(it))
some_list[2] = 10
</code>
This prints <code>0</code> in CPython (all versions), but the behavior is not specified by the language. That said, it's the only thing that makes sense in the wider context of Python's dynamic nature.

