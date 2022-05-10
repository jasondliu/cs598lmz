from types import FunctionType
a = (x for x in [1])
b = range(2)
c = map(lambda x:x, [3])
d = filter(lambda x:True, [4])
e = FunctionType(lambda x:x, globals(), 'name')

# __slots__
class AutoClass(object):
    __slots__ = ['attr1']
    def __init__(self):
        self.attr1 = 1
    def __setattr__(self, name, value):
        if name not in self.__slots__:
            raise Exception('ERROR: invalid attribute: ' + name)
        object.__setattr__(self, name, value)
    def __repr__(self):
        return 'AutoClass(%s)' % self.attr1

# __repr__, __str__
class ReprClass(object):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return 'ReprClass(%r)' % self.value
    def __str__(self):
        return 'str: %s' % self
