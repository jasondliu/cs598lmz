import gc, weakref

class A(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)
d = weakref.WeakValueDictionary()
d['primary'] = a
print 'before del a'
print d['primary']
del a
print 'after del a'
gc.collect()
print d['primary']

# before del a
# 10
# after del a
# 10
# Traceback (most recent call last):
#   File "weakref_weakvaluedictionary.py", line 17, in <module>
#     print d['primary']
#   File "/usr/lib/python2.7/weakref.py", line 38, in __getitem__
#     o = self.data[key]()
# KeyError: 'primary'
