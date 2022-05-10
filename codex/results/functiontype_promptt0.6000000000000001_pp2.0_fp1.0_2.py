import types
# Test types.FunctionType, types.BuiltinFunctionType, types.MethodType, types.BuiltinMethodType

def f1():
    pass

f2 = f1

def f3(a):
    pass

class C:
    def f4(self):
        pass

    f5 = f4

    def f6(self, a):
        pass

c = C()

test_types = [
    (f1, types.FunctionType),
    (f2, types.FunctionType),
    (f3, types.FunctionType),
    (C.f4, types.MethodType),
    (C.f5, types.MethodType),
    (C.f6, types.MethodType),
    (c.f4, types.MethodType),
    (c.f5, types.MethodType),
    (c.f6, types.MethodType),
]

for item, expected_type in test_types:
    print('{} is {}'.format(item, expected_type))
    assert type(item) is expected_type, '{} is not
