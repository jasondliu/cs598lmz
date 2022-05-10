fn = lambda: None
# Test fn.__code__ and fn.__closure__ attributes
print("From Function Object:")
print("\tmodule: %s" % fn.__module__)
print("\tdef: %s" % fn.__code__.co_name)
print("\treturn: %s" % fn.__code__.co_flags)
print(fn.__dict__)
print("\t__dict__ = %s" % fn.__dict__)
print("\t__name__ = %s" % fn.__name__)
print("\t__doc__ = %s" % fn.__doc__)
# Test fn.__closure__ attributes
print(fn.__closure__)
# Test fn.__code__ attributes
print("\tco_argcount = %s" % fn.__code__.co_argcount)
print("\tco_consts = %s" % fn.__code__.co_consts)
print("\tco_varnames = %s" % fn.__code__.co_varnames)
print("\tco_names = %s
