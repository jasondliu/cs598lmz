import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect reordering of objects' tp_clear slots
# Note: weaklist.clear() and weaklist.__init__() are
# written in Pyrex, and take a "previous" argument.
# The goal of this test is to find out whether some
# combination of object reordering and multiprocessing
# causes problems for that implementation.
import weakref
def append(prev, item):
    prev.append(item)
    print "appended ",item
    return prev
def clear(prev, i = None):
    global list
    prev.clear(i)
    list = weakref.WeakList(prev)
    print "cleared", i
    return prev

list = weakref.WeakList()
x0 = []
expect_gc = []
objs = []
map(append, [x0] * 3, [expect_gc] * 3)
map(clear, [list] * 3, range(3))
list = None
import gc
del x0, expect_gc, objs
gc.collect()
