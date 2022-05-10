import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
for i in range(5):
    print(gc.collect())


a = weakref.WeakKeyDictionary()
b = {}
print(gc.get_referents(a))
print(objgraph.typestats(gc.get_referents(a)))
print(gc.get_referents(b))
print(objgraph.typestats(gc.get_referents(b)))

a['a'] = 'aaa'
b['b'] = 'bbb'
print(gc.get_referents(a))
print(objgraph.typestats(gc.get_referents(a)))
print(gc.get_referents(b))
print(objgraph.typestats(gc.get_referents(b)))

del a
del b
print(gc.collect())
objgraph.show_backrefs(gc.garbage[0])
objgraph.show_backrefs(gc.garbage[1])
objgraph.show_backrefs([o for o in gc.garbage if 'bb
