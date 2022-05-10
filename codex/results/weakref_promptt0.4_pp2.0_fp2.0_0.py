import weakref
# Test weakref.ref
class Foo(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name

obj = Foo('obj')
r = weakref.ref(obj)
print(r)
print(r())
print(obj)

del obj
print(r())

class MyList(list):
    '''
    A subclass of list.
    '''
    def __init__(self, *args):
        super().__init__(*args)
        self._removed_items = []
    def __delitem__(self, index):
        self._removed_items.append(self[index])
        super().__delitem__(index)
    def removed_items(self):
        return self._removed_items
    def __repr__(self):
        return 'MyList(%s)' % list.__repr__(self)

myl = MyList(['item'])
print(myl)
del myl[0]
print(myl.removed
