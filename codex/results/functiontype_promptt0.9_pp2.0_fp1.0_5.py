import types
# Test types.FunctionType to check callable
callable(pypyjs.hello)

# Failing test, no has_key attribute
pypyjs.has_key('name')

# Failing test, no has_key attribute
hasattr('name')

# Failing test, no has_key method
pypyjs.Property.has_key = lambda x: True

# Failing test
pypyjs.Property.__set__ = lambda x,y: True

# Failing test
pypyjs.Property.setter = lambda x,y: True

# Failing test
pypyjs.Property.__name__ = 'Property'

# Failing test
pypyjs.Property.__name__ = None


pypyjs.revdict.html
# Failing test
x = "self.__doc__"
dict(x)

# Failing test
dict(globals())

# Failing test
pypyjs.walk_code(None)

# Failing test
pypyjs.walk_code({})

# F
