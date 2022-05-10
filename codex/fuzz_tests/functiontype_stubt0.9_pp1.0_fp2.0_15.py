from types import FunctionType
a = (x for x in [1])
b = list(x for x in [1, 2])
c = {x for x in [1, 2]}
d = {'x': x for x in [1, 2]}
assert type(a) == generator
assert type(b) == list
assert type(c) == set
assert type(d) == dict
assert isinstance(function, FunctionType)


# Iterator
class BadIterator():
    pass


class ListIterator():

    def __init__(self, l):
        self.l = l

    def __iter__(self):
        return self

    def next(self):
        return self.l.pop()


l = [1, 2, 3]
i = iter(l)
assert isinstance(i, ListIterator)
assert repr(i) == '<ListIterator object at 0x%x>' % id(i)
assert i.next() == 1
assert isinstance(i, ListIterator)
assert repr(i) == '<ListIterator object at 0x%x>' % id(i)
assert i.next() == 2
assert
