import weakref
# Test weakref.ref(None) and weakref.ref(obj) with and without callback.

a = []

for t in ( None, None, None ):
    a.append( weakref.ref(t) )

