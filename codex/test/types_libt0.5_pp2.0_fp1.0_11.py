import types
types.MethodType(lambda self: None, None, object)

class C:
    def method(self):
        pass

c = C()

# replace a method
c.method = types.MethodType(lambda self: None, c)

# add a new class method
C.method = types.MethodType(lambda self: None, None, C)

# add a new instance method
c.method = types.MethodType(lambda self: None, c)

class D(C):
    def method(self):
        print("D")

d = D()

# replace a method
d.method = types.MethodType(lambda self: None, d)

# add a new class method
D.method = types.MethodType(lambda self: None, None, D)

# add a new instance method
