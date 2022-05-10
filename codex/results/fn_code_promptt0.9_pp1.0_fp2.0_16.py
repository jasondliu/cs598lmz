fn = lambda: None
# Test fn.__code__.co_argcount after classe definitions
class A(object):
    def f(self):
        fn()

    def f(self, *args):
        fn()

    def f(self, *args, **kwargs):
        fn()

    def f(self, arg1):
        fn()

    def f(self, arg1, arg2):
        fn()

    def f(self, arg1, arg2, arg3):
        fn()

assert A.f.__code__.co_argcount == 3  # *args and **kwargs are excluded

class B(object):
    def f(self):
        fn()

    def f(self, *args):
        fn()

    def f(self, *args, **kwargs):
        fn()

    def f(self, arg1, arg2):
        fn()

    def f(self, arg1, arg2, arg3):
        fn()

assert B.f.__code__.co_argcount == 3  # *args and **kwargs are excluded

class C(
