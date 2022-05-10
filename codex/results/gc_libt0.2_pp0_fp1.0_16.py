import gc, weakref

class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'd["primary"] =', d['primary']
del a
gc.collect()
print 'd["primary"] =', d['primary']

# d["primary"] = 10
# d["primary"] = None
