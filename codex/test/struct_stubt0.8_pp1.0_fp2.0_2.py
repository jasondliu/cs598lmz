from _struct import Struct
s = Struct.__new__(Struct)
t = Struct.__new__(Struct)
s.format = t.format = "=B"


class MyObject(object):
    __slots__ = "foo", "bar"

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar


class MyDict(dict):
    pass


class MyList(list):
    pass


class MyObjectWithSlots(object):
    __slots__ = "foo", "bar"
    mylist = MyList
    mydict = MyDict

    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar
        self.mylist.extend(self.mydict)

    def __reduce__(self):
        return self.__class__, (self.foo, self.bar)


class ListSubclass(list):
    pass


class SetSubclass(set):
    pass


class TupleSubclass(tuple):
    pass


