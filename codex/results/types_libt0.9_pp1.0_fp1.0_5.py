import types
types.FunctionType.f_locals

def outer(x, y = 6):
    def inner():
        return x
    return inner

res = outer(100, 69)
res.__closure__
print res.__closure__[0].cell_contents

# now modify x and see what happens

x = 99
res()

print res.__closure__[0].cell_contents

def outer(x, y = 6):
    def inner():
        return x
    return inner

outer(100, 69)(99)
