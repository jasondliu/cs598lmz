import types
# Test types.FunctionType and types.LambdaType

# Lambdas are not instances of FunctionType
def test(expected, actual):
    if expected != actual:
        print("FAILED: Expected", expected, "but was", actual)
    else:
        print("PASSED")

l = lambda x: x
test("lambda", str(type(l)))
test(False, isinstance(l, types.FunctionType))

def f(x):
    return x

test("function", str(type(f)))
test(True, isinstance(f, types.FunctionType))


def f2(x, y):
    return x * y

h = lambda: f2(2, 3)

test("40", h())
