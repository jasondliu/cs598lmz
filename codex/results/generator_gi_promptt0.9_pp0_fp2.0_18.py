gi = (i for i in ())
# Test gi.gi_code is None currently. Since this also depends on a code
# object is created, put it in "test_code"
# cp3 = code_property(gi)
# Test a wrapped generator
def gen():
    i = 1
    while 1:
        yield i
        i += 1
gi = gen()
cp3 = code_property(gi)

class P(object):

    def f(self):
        pass

    def __call__(self):
        pass

class A(object):

    class B(object):

        @classmethod
        def f(cls, arg="spam"):
            pass

        @staticmethod
        def g(arg="spam"):
            pass

    def f(self):
        pass
    def __add__(self, other):
        pass
    def __call__(self):
        pass
    def __cmp__(self, other):
        pass
    __getitem__ = P()

class C(object):
    @staticmethod
    def f(arg="spam"):
        pass
    f = staticmethod
