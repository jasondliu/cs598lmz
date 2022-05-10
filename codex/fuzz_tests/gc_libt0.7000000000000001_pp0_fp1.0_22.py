import gc, weakref

wref_to_object = weakref.ref(o)

if wref_to_object() is not None:
    print("wref_to_object still has a reference!")

o = None
gc.collect()

if wref_to_object() is None:
    print("wref_to_object does not have a reference!")
