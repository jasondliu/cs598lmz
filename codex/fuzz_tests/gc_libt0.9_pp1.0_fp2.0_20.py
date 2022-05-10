import gc, weakref, contextlib

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


def weakref_callback(obj, data=None):
    if data is not None:
        print(data)
    obj = None

print('Child:')
child = Child()
child_ref = weakref.ref(child, weakref_callback)
del child
print('\nChild:')
gc.collect()
print('\nMisc:')
misc_parent = MiscParent()
misc_parent_ref = weakref.ref(misc_parent, weakref_callback)
misc_grandparent = MiscGrandparent()
misc_grandparent_ref = weakref.ref(misc_grandparent, weakref_callback)
misc_descendant = MiscDescendant()
misc_descendant_ref = weakref.ref(misc_descendant, weakref_callback)
del misc_parent, misc_grandparent, misc_descendant
print('\nMisc:')
gc.collect()
print('\nParents:')
parent = Parent()
parent_ref = weakref.ref(parent
