import weakref
# Test weakref.ref(obj)

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

a = Foo('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

del a
d['primary']

# Test weakref.ref(obj, callback)

class Foo(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Foo({!r})'.format(self.name)

a = Foo('a')
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary']

def callback(wr):
    print('callback({!r})'.format(wr))

wr = weakref.ref(a, callback)

del a
d['primary']

# Test weakref.ref(obj, callback)

