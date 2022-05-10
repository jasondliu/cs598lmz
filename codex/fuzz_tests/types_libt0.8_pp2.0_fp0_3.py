import types
types.ClassType
print type(1)
print type('str')
print type(u'unicode')
print type([])
print type({})
print type(object)

def func(): pass
print type(func)
print type(xrange)

class MyClass:
    def __init__(self):
        self.data = []
        self.index = 0
    def __getitem__(self):
        return self.data[self.index]
    def __setitem__(self, index, value):
        self.data[index] = value
    def __len__(self):
        return len(self.data)
ins = MyClass()
print type(ins)

class MyMetaClass(type):
    def __call__(cls, *args, **kwargs):
        print '__call__ of %s' % cls
        print 'args =', args
        print 'kwargs =', kwargs
        obj = cls.__new__(cls, *args, **kwargs)
        cls.__init__(cls, *
