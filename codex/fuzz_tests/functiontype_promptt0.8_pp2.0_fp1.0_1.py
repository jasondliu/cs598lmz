import types
# Test types.FunctionType

def f(): pass

try:
    class BadF(types.FunctionType): pass
except TypeError as e:
    print(e.args)

@types.FunctionType
def g(): pass

print(g)

def h(x):
    def i(y):
        def j(z):
            return z
        return y
    return x

class j(types.FunctionType):
    def __call__(self, y):
        def i(z):
            return z
        return y

print(j)
print(j()(7))
