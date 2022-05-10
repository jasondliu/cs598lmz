import ctypes
# Test ctypes.CField object, by checking that the appropriate
# AttributeError is raised when trying to instantiate.

foo = ctypes.CField("_foo")
print("foo is", repr(foo))
# accessing all attributes must fail
def check_ctype_readonly_attributes(test):
    for attribute in ('input', 'output', '_length_', '_type_'):
        try:
            value = getattr(test, attribute)
        except AttributeError as e:
            err = e
        else:
            print("value for {attr} is {val}".format(attr=attribute, val=value))
        if err is None:
            print("failed to raise AttributeError for {attr}".format(attr=attribute))

check_ctype_readonly_attributes(foo)
