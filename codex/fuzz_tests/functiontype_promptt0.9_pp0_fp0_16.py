import types
# Test types.FunctionType

def make_adder(n):
    def adder(x):
        return x+n
    return adder

a1 = make_adder(1)
a2 = make_adder(2)

print(types.FunctionType(a1.__code__), a1((a2(3))))
