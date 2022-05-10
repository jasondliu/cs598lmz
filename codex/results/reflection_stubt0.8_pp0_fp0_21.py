fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__closure__ = (fn,)
fn()

class A(object):
    def __call__(self):
        print 'A call'
a = A()
b = A()

class M(type):
    pass

class R(object):
    __metaclass__ = M

r = R()

class B(object):
    __slots__ = ['__dict__', 'other']

b = B()
b.other = 'blah'
b.other = 'b'

class C(object):
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        return self.val == other.val
    def __lt__(self, other):
        return self.val < other.val
    def __le__(self, other):
        return self.val <= other.val
    def __ne__(self, other):
        return self.val != other.val
    def __gt__(self, other):
        return self.val
