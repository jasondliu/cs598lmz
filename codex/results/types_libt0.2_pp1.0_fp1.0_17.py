import types
types.MethodType(lambda self: None, None, None)

# This should not crash
class A:
    def __init__(self):
        self.x = 1

a = A()
a.x = 2

# This should not crash
class B:
    def __init__(self):
        self.x = 1

b = B()
b.x = 2

# This should not crash
class C:
    def __init__(self):
        self.x = 1

c = C()
c.x = 2

# This should not crash
class D:
    def __init__(self):
        self.x = 1

d = D()
d.x = 2

# This should not crash
class E:
    def __init__(self):
        self.x = 1

e = E()
e.x = 2

# This should not crash
class F:
    def __init__(self):
        self.x = 1

f = F()
f.x = 2

# This should not crash
class
