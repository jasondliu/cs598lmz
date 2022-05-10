fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn()

# Descriptor protocol not respected for __new__
class Descr(object):
    def __get__(self, obj, objtype=None):
        return "Descr"
    def __set__(self, obj, value):
        pass

class C(object):
    __new__ = Descr()

C()

# Bug #1345: __new__ can be overridden by a staticmethod
class C(object):
    def __new__(cls):
        return super(C, cls).__new__(cls)

C.__new__ = staticmethod(lambda cls: None)
C()

# Bug #1347: __new__ called with wrong arguments
class C(object):
    def __new__(cls, a):
        return super(C, cls).__new__(cls)

C(1)

# Bug #1348: __new__ can be overridden by a classmethod
class C(object):
    def __new__(cls):
        return super
