import gc, weakref, sys

class Object(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Object(%s)' % self.name

obj = Object('obj')
p = weakref.proxy(obj)

print('BEFORE:', p.name)
obj = None
gc.collect()
try:
    print('AFTER:', p.name)
except ReferenceError:
    print('AFTER:', sys.exc_info()[1])
