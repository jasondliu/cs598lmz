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
del view

# Test that uncollectable objects are not allowed to go away
# immediately.
def test_del_ss():
    class C:
        def __del__(self):
            global ss
            ss = "dead"
    c1 = C()
    ss = "alive"
    objgraph.show_backrefs([c1], filename=None)
    del c1
    objgraph.show_backrefs([], filename=None)
    assert ss == "alive", "dead object went away immediately?!"

# Issue #3259: refcycle-prone code in C code
import marshal, struct
