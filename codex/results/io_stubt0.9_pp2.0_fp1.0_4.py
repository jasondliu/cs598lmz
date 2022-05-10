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
import gc
gc.collect()
heap()
""")
    def test_large_allocation(self, space):
        # a stress test to make sure we don't run out of stack
        space = self.space
        w_res = space.appexec([], """():
import gc; gc.disable()
r = range(10**9)
r[0] = r[3] + r[1]
r[3:3] = r
r[:] = r
r[1::2] == r
v = []
for i in range(10):
    v.append(r[-1])
del r
gc.collect()
v
""")
        assert space.unwrap(w_res) == [1000000000] * 10

    def test_field_write_barrier(self, space):
        space.appexec([], """
l = []
def f(p):
    l.append(p)
gc.write_barrier(f)

t = [1]
t[0] = 1
t[
