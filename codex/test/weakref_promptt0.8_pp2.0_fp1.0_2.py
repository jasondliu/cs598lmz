import weakref
# Test weakref.ref() on dicts.
class A(object):

    def __init__(self, name):
        self.name = name


class B(object):

    def __init__(self):
        self.d = {}

    def add(self, item):
        self.d[item.name] = item


def foo(x):
    return x.name


a = A('a')
b = B()
b.add(a)
r = weakref.ref(b.d, foo)

class C(object):

    def __init__(self, dict):
        self.d = dict

    def __repr__(self):
        return 'C(%s)' % self.d
# Test weakref.ref() on dicts.
class A(object):

    def __init__(self, name):
        self.name = name


class B(object):

    def __init__(self):
        self.d = {}

    def __getitem__(self, key):
        return self.d[key]

