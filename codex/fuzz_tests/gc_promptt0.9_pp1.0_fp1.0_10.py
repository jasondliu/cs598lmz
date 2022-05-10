import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() with uncollectable garbage.
# There are four objects:
#
#   * myset: a collectable set object.  Initially contains integers 0, 1, 2.
#   * myref: a reference to myset.
#   * cyclic_lst: a list containing myref.
#   * a dict which contains cyclic_lst.
#
# myset should be collected, but the other objects should not.  With
# Python 2.1a1 and later, there can be an arbitrary number of pyints
# that are not collected as long as dictobject.c::lookdict_string() is
# used.

myset = {1,2,3}
myref = weakref.ref(myset)
cyclic_lst = [myref]
a_dict = {ASP*3:cyclic_lst}

gc.collect()
if myset:
    print("myset is not collected")

if not myref():
    print("failure of myref")

if cyclic_lst:
    print("cyclic_lst is not
