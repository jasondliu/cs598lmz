import types
types.MethodType(lambda self, args: None, None, Test)

# Test that we don't crash when we see a class that inherits from
# something we can't find (in this case, 'object').
class Test(object):
    pass
types.MethodType(lambda self, args: None, None, Test)

# Test that we don't crash when we see a class that inherits from
# something that we can't find (in this case, 'object').
class Test(object):
    pass
types.MethodType(lambda self, args: None, None, Test)

# Test that we don't crash when we see a class that inherits from
# something that we can't find (in this case, 'object').
class Test(object):
    pass
types.MethodType(lambda self, args: None, None, Test)

# Test that we don't crash when we see a class that inherits from
# something that we can't find (in this case, 'object').
class Test(object):
    pass
types.MethodType(lambda self, args: None, None, Test)


