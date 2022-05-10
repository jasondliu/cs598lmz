import types
# Test types.FunctionType
#
# This test checks that the types.FunctionType class constructor
# is able to create instances of the FunctionType type.
#
# This test is constructed so that it will fail if the
# types.FunctionType constructor fails.

#
#######################
#

def test_types_functiontype_class():
    class C:
        def __init__(self, f):
            self.f = f
        def call(self):
            return self.f()

    def f():
        return 2

    c = C(f)

    assert c.call() == 2


#
#######################
#

def test_types_functiontype_class_exception():
    class C:
        def __init__(self, f):
            self.f = f
        def call(self):
            return self.f()

    def f():
        raise Exception("exception")

    c = C(f)

    with pytest.raises(Exception):
        c.call()

    assert True

#
#######################
#

def test_types_
