import types
types.MethodType(lambda self: self.__class__.__name__, None)

# %%
class A:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return f'A({self.x})'

# %%
a = A(1)
a

# %%
a.__repr__()

# %%
a.__str__()

# %%
str(a)

# %%
repr(a)

# %%
class A:
    def __init__(self, x):
        self.x = x
    def __repr__(self):
        return f'A({self.x})'
    def __str__(self):
        return f'A({self.x})'

# %%
a = A(1)
a

# %%
str(a)

# %%
repr(a)

# %%
class A:
    def __init__(self, x):
        self.x = x
    def __repr__
