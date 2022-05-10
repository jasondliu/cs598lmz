import weakref
# Test weakref.ref() and weakref.proxy()
# Listing 1
class ExpensiveObject:
    def __del__(self):
        print('(Deleting %s)' % self)

def callback(reference):
    """Invoked when referent is garbage collected"""
    print('callback(', reference, ')')

obj = ExpensiveObject()
r = weakref.ref(obj, callback)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())

# Listing2
class ExpensiveObject:
    def __del__(self):
        print('(Deleting %s)' % self)

obj = ExpensiveObject()
r = weakref.ref(obj)
p = weakref.proxy(obj)

print('via obj:', obj.attribute)
print('via ref:', r().attribute)
print('via proxy:', p.attribute)

print('deleting obj')
del obj
