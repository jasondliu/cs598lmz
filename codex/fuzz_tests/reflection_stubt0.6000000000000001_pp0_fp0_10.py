fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi

# test __code__ on a class
class A:
    pass

A.__code__ = gi

# test __code__ on a class instance
a = A()
a.__code__ = gi

print("Done.")
