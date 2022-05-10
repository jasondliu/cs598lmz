import gc, weakref, sys
#print(dir(gc)) # to discover what you can count for

class A:
    def __del__(self):
        print('A.__del__')
a = A()
wref = weakref.ref(a)
print('before:', sys.getrefcount(a))

wref() # produces None if a was collected
r = wref()
r is None
del a
gc.collect()

