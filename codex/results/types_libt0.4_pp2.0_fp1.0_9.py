import types
types.MethodType(lambda self: self.x, None, A)

# Test that we can subclass a builtin type
class B(str):
    pass

# Test that we can call a builtin type
str()

# Test that we can override a builtin type
class C(list):
    def __init__(self, x):
        self.x = x

# Test that we can call an overridden builtin type
C([1, 2, 3])

# Test that we can override a builtin type method
class D(list):
    def __init__(self, x):
        self.x = x
    def __len__(self):
        return self.x

# Test that we can call an overridden builtin type method
len(D(42))

# Test that we can override a builtin type method
class E(list):
    def __init__(self, x):
        self.x = x
    def __len__(self):
        return self.x
    def __getitem__(self, key):
        return 42

# Test
