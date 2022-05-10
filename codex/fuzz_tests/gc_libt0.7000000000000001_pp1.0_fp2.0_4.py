import gc, weakref

class Dummy:
    pass

d = Dummy()

# referencing d from the global dictionary
globals()["dummy"] = d

# now d has two references, including the global dictionary
print(gc.get_referents(d))

# now delete the global dictionary reference
del globals()["dummy"]

print(gc.get_referents(d))

wref = weakref.ref(d)
print(wref)
print(wref())

del d

print(wref)
print(wref())
