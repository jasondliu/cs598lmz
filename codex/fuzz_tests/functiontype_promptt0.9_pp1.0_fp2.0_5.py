import types
# Test types.FunctionType by recycling code from test_types.py
def nested(a, b, c=1, *args):
    def nested2(alpha, beta):
        x = alpha + beta
        return x
    v = a + b + c
    v2 = nested2(args[0], args[1])
    return v + v2

class C(object):
    def nested(self, a, b, c=1, *args):
        def nested2(alpha, beta):
            x = alpha + beta
            return x
        v = a + b + c
        v2 = nested2(args[0], args[1])
        return v + v2

# Just a reference to know what this is supposed to return
def test_expected_for_test_nested_func():
    return 63

def test_nested_func():
    return nested(10, 20, 30, 40, 50)

def test_nested_func_name():
    return nested.__name__

def test_nested_func_defaults():
    return nested.__defaults__
