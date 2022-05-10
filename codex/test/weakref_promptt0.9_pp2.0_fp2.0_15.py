import weakref
# Test weakref.ref and weakref.proxy.
# Tests of the predicates weakref.ref() and weakref.proxy()
# not included because they are implicitly tested below.

x = "Hello"


class A:

    def goodbye(self):
        return 'Goodbye'


a = A()
