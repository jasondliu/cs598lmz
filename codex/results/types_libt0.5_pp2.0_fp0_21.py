import types
types.MethodType(lambda self: None, None, D)

# Make sure we can still create new methods #############################

def f(self): pass
D.method = types.MethodType(f, None, D)
D.staticmethod = staticmethod(f)
D.classmethod = classmethod(f)

# Make sure we can still create new methods, even if ob_type is not set #

del D.__dict__["__class__"]
def f(self): pass
D.method = types.MethodType(f, None, D)
D.staticmethod = staticmethod(f)
D.classmethod = classmethod(f)

# Test __doc__ and __name__ #############################################

def f(self):
    """This is a method docstring"""
    pass
D.method = types.MethodType(f, None, D)
assert D.method.__doc__ == "This is a method docstring"
assert D.method.__name__ == "f"

# Test instancemethods ###################################################

class E:
    def f(
