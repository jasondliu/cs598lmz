import gc, weakref

gc.set_debug(gc.DEBUG_LEAK)

class C:
    def __del__(self):
        print("__del__ called")

def f():
    c = C()
    print("f() returns")

print("creating cycle...")
f()
print("referring to cycle...")
wr = weakref.ref(c)
print("forgetting cycle...")
del c
print("collecting...")
gc.collect()
print("cleaning up...")
for i in range(2):
    wr()
    print("collecting...")
    gc.collect()
    print("done")
