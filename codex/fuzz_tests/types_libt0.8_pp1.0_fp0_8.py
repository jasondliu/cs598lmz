import types
types.MethodType(method, object)

# Build a method out of a function.
# The function is passed in explicitly.
class C:
    pass
def f1(self, x, y):
    return min(x, x+y)

a = C()
a.f = types.MethodType(f1, a)

print(a.f(3, 4))

## 
