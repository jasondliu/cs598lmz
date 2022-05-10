import types
# Test types.FunctionType

class A(object):

    def foo(self):
        pass

    def bar(self):
        pass

def test(expected_len, expected_items):

    cls_dict = A.__dict__
    assert len(cls_dict) == expected_len

    for (k, v) in expected_items:
        assert cls_dict[k] is v

expected_len = 2
expected_items = [('bar', A.bar), ('foo', A.foo)]
test(expected_len, expected_items)

class A(object):
    bar = None
    def foo(self):
        pass
    bar = types.MethodType(bar, None, A)

expected_len = 2
expected_items = [('foo', A.foo), ('bar', A.bar)]
test(expected_len, expected_items)

# Test types.UnboundMethodType (functions & methods)

class B(object):
    def __init__(self, v):
        self.v = v
    def foo(self, x, y
