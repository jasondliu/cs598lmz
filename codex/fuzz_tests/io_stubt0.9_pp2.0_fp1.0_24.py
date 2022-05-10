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
What happens is that even though the <code>f</code> variable goes out of scope, the <code>io.BufferedReader</code> object still has a reference to it. So even though those <code>readinto</code> and <code>readable</code> functions belong to the global scope anymore, their enclosing scope from their creation is kept alive by the <code>io.BufferedReader</code> object. (See this previously asked question, relating to whether the Python interpreter keeps entire stack frames alive as long as there're any references to objects within those stack frames.)
Now, you're probably wondering, but why does <code>gdbm</code> not show this problem, yet it, too, is implemented in pure Python. The answer is that even though the <code>gdbm</code> module is written in Python (at least on my system), it's actually implemented in the C API, which isn't subject to the same constraints (at least as far as I'm aware). So this isn't an actual "bug" with <code>io</code>; it's just a feature of CPython's implementation that also happens to have useful
