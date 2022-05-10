import types
types.MethodType(lambda self: self.__class__.__name__, None)

# %%
class A:
    def __init__(self, x):
        self.x = x
