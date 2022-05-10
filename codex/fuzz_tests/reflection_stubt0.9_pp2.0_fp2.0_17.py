fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del fn    # forces gi to be freed

f= lambda: None; del f
try:
    raise StopIteration
except StopIteration:
    pass
print("# the tp_dealloc for a type with only weakrefs should be called even"
      " if there is a pending exception")
n = None
try:
    raise RuntimeError
except RuntimeError as e:
    w = weakref.ref(e)

del e
print("# test that there are no builtin objects left on the heap")
def showsize(a):
    print("%d bytes (%d KB)" % (a, a//1024))

# get the size
refs = (weakref.ref(sys),)
after = before = gc.collect()

# create a bunch of objects
for i in range(1000):
    gi = (i for i in ())
    for j in range(3):
        refs += gi, weakref.ref(gi),
    for j in range(5):
        exec("pass", {}, {'gi':gi})

