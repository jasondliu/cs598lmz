import gc, weakref

class Counter(object):
    def __init__(self):
        self.counter = 0

    def __call__(self):
        self.counter += 1
        return self.counter

counter = Counter()

class ExpensiveObject(object):
    def __del__(self):
        print '(Deleting %s)' % self

    def __repr__(self):
        return 'ExpensiveObject(%s)' % self.__dict__

def get_expensive_object():
    obj = ExpensiveObject()
    obj.id = counter()
    return obj

obj = get_expensive_object()
d = weakref.WeakValueDictionary()
d['primary'] = obj
d['primary']
d['primary']
d['primary'].id
d['secondary'] = get_expensive_objec
