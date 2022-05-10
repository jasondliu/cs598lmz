import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()
gc.collect()
# Collectable objects:
[id(o) for o in gc.get_objects() if isinstance(o, MyClass)]

# Test __del__
m = MyClass()
m = None
gc.collect()
# Collectable objects:
[id(o) for o in gc.get_objects() if isinstance(o, MyClass)]


# Test weakrefernce
m = MyWeakClass()
print(m.__dict__)
m = None
gc.collect()
print(m.__dict)
# Collectable objects:
[id(o) for o in gc.get_objects() if isinstance(o, MyClass)]
</code>
The output is:
<code>MyClass instance at 0x53f340
{'_MyClass__a': 1}
{'_MyWeakClass__a': 1}
*** Collectable objects ***
{'_MyWeakClass__a': 1}
{'_MyWeakClass__a': 1}
</code>
I have a couple of questions:

Why <code>
