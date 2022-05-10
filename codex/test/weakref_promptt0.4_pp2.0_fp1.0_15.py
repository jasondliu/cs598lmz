import weakref
# Test weakref.ref(x) == weakref.ref(x) for various x

class Foo(object):
    pass

class Foo2(object):
    def __eq__(self, other):
        return True

class Foo3(object):
    def __eq__(self, other):
        return False

class Foo4(object):
    def __hash__(self):
        return 42

class Foo5(object):
    def __eq__(self, other):
        return False
    def __hash__(self):
        return 42

class Foo6(object):
    def __eq__(self, other):
        return True
    def __hash__(self):
        return 42

class Foo7(object):
    def __eq__(self, other):
        return True
    def __hash__(self):
        return 42
    def __call__(self):
        pass

class Foo8(object):
    def __eq__(self, other):
        return True
    def __hash__(self):
        return 42
