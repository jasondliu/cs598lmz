import types
# Test types.FunctionType
def foo():
    pass

class A:
    def __init__(self, x):
        self.x = x
    def bar(self):
        self.x += 1
    def __call__(self):
        self.x += 2
    def __getitem__(self, y):
        self.x += y

a = A(1)
b = A(2)

print(a.x)
print(b.x)

a.bar()
b.bar()

print(a.x)
print(b.x)

a()
b()

print(a.x)
print(b.x)

a[3]
b[3]

print(a.x)
print(b.x)

print(type(foo) is types.FunctionType)
print(type(A.bar) is types.FunctionType)
print(type(A.__init__) is types.FunctionType)
print(type(A.__call__) is types.FunctionType)
print(type(A.__get
