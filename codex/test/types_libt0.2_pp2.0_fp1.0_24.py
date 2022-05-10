import types
types.MethodType(lambda self: None, None, cls)

# This should not crash
class C:
    def __init__(self):
        self.x = 1

C()

# This should not crash
class D:
    def __init__(self):
        self.x = 1

D()

# This should not crash
class E:
    def __init__(self):
        self.x = 1

E()

# This should not crash
class F:
    def __init__(self):
        self.x = 1

F()

# This should not crash
class G:
    def __init__(self):
        self.x = 1

G()

# This should not crash
class H:
    def __init__(self):
        self.x = 1

H()

# This should not crash
class I:
    def __init__(self):
        self.x = 1

I()

# This should not crash
