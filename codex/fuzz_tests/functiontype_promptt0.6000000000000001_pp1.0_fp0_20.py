import types
# Test types.FunctionType
def test(func):
    if isinstance(func, types.FunctionType):
        print("Good")
    else:
        print("Bad")

test(lambda x: x)
test(test)

# Test types.MethodType
def test2(method):
    if isinstance(method, types.MethodType):
        print("Good")
    else:
        print("Bad")

class C:
    def method(self):
        pass

c = C()
test2(c.method)

# Test types.BuiltinFunctionType
def test3(func):
    if isinstance(func, types.BuiltinFunctionType):
        print("Good")
    else:
        print("Bad")

test3(print)
test3(test3)

# Test types.BuiltinMethodType
def test4(method):
    if isinstance(method, types.BuiltinMethodType):
        print("Good")
    else:
        print("Bad")

test4(str.lower)
test4(test4)

# Test types.L
