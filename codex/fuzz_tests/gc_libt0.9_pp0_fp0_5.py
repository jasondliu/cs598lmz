import gc, weakref

class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # create a reference
d = weakref.WeakValueDictionary()
d['primary'] = a            # does not create a reference
d['primary']                # fetch the object if it is still alive
a = None					# remove the one reference
gc.collect()                # run garbage collection right away

print 'd dictionary'.title()
print d

print
print 'd list'.title()
print list(d)

print
print 'd values'.title()
print d.values()



# by definition de diccionario se está creando una referencia al objeto
# como podemos observar a continuación:
a = A(10)
refs = [weakref.ref(a)]			# 1
print refs[0].__call__()

# Sin embargo, esto ya no sucede al us
