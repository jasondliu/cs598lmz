import types
types.SimpleNamespace(header="10", attrib="foo", value="bar")

# Advantages of SimpleNamespace (over regular namedtuples)
#


# 1. Dot-lookup
x = AttrClass()
x.foo
# or
getattr(AttrClass, 'foo')

# however, in the namedtuple, we get
# TypeError: 'namespace' object has no attribute 'foo'
# We cannot access the vers attribute easily since this is evaluated as a string.
# So we need to tell it to treat vers as an attribute like so:

x = AttrClass()
x[0]  # 'foobar'
x.vers  # TypeError: 'namespace' object has no attribute 'foo'
AttrClass._fields[2]  # 'vers'
x[AttrClass._fields[2]]  # '10'

# using dot lookup is more explicit and avoids mistakes

# 2. Built-in version
# No need to:
# from collection import namedtuple
x = types.SimpleNamespace(foo="bar")

# 3.
