import gc, weakref

class Test(object):
    def __init__(self, name):
        self.name = name
        print 'Created', self.name

    def __del__(self):
        print 'Destroyed', self.name

def func():
    t = Test('local')
    print 'func() returning'

t = Test('global')
r = weakref.ref(t)
print 'before func()'
func()
print 'after func()'
print 't:', t
print 'r:', r
print 'r():', r()
print 'deleting t'
del t
print 'r():', r()
print 'collecting'
gc.collect()
print 'r():', r()
