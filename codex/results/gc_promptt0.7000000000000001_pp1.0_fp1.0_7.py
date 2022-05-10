import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect().  This should collect the last two objects.
def f():
    x = [1,2]
    y = [3,4]
    del x
    del y
    gc.collect()

f()

# Check that collecting twice clears away the garbage.
gc.collect()

# Check that finalizers are run.
def onFinalize(obj, what):
    print "finalizing", what

class OnFinalize:
    def __init__(self, what):
        self.what = what
    def __del__(self):
        print "finalizing", self.what

lf = [OnFinalize("list"), OnFinalize("list")]
lw = [weakref.ref(OnFinalize("list")), weakref.ref(OnFinalize("list"))]
td = {1: OnFinalize("dict"), 2: OnFinalize("dict")}
tw = {1: weakref.ref(OnFinalize("dict")), 2: weakref.ref(OnFinalize("dict"))}

lf2 = [lf, lw, td, tw]
