import weakref

class A(object):
    pass

a = A()
d = weakref.WeakValueDictionary()
d['primary'] = a
print('d["primary"]= ', d['primary'])
del a
print('d["primary"]= ', d['primary'])
