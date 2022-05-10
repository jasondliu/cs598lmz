import gc, weakref

class SimpleObject:
    def __init__(self, name):
        self.name = name
    def __repr__ (self):
        return 'SimpleObject({0})'.format(self.name)


def on_finalize(arg):
    print('on_finalize({0})'.format(arg))

obj = SimpleObject('obj')
f = weakref.finalize(obj, on_finalize, 'obj goes away')
del obj
f
