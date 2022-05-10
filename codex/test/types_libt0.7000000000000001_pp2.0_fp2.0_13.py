import types
types.MethodType(lambda self, a, b, c: None, None, A)

# Verify that types.MethodType does not allow creating a method that
# does not correspond to an actual method descriptor.
try:
    types.MethodType(lambda self: None, None, A)
except TypeError:
    pass
else:
    print("Did not raise TypeError")

# Verify that types.MethodType does not allow creating a method with
# incorrect self parameter.
try:
    types.MethodType(A.meth, None, A)
except TypeError:
    pass
else:
    print("Did not raise TypeError")

# Verify that types.MethodType does not allow creating a method with
# a non-class owner.
try:
    types.MethodType(A.meth, None, A())
except TypeError:
    pass
else:
    print("Did not raise TypeError")

# Verify that types.MethodType does not allow creating a method if owner
