fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = 'fn'
fn.__doc__ = 'doc'

class C:
    def __init__(self):
        self.__doc__ = 'doc'
        self.__name__ = 'name'
        self.__module__ = 'mod'
        self.__dict__ = {'a': 1}
        self.__class__ = type(self)
    def __call__(self):
        pass
    def __get__(self, obj, objtype=None):
        pass
    def __set__(self, obj, value):
        pass
    def __delete__(self, obj):
        pass

class D(C):
    def __init__(self):
        C.__init__(self)
        self.__class__ = C

class E(C):
    def __init__(self):
        C.__init__(self)
        self.__class__ = type(self)

class F(C):
    def __init__(self):
        C.__init
