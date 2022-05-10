import types
types.MethodType(lambda self: self.foo, obj)

# TypeError: can't set attributes of built-in/extension type 'object'
# obj.foo = lambda self: self.foo

# TypeError: can't set attributes of built-in/extension type 'object'
# obj.__class__.foo = lambda self: self.foo

# TypeError: can't set attributes of built-in/extension type 'object'
# obj.__class__.__dict__['foo'] = lambda self: self.foo

# TypeError: can't set attributes of built-in/extension type 'object'
# obj.__class__.__dict__.update({'foo': lambda self: self.foo})

# TypeError: can't set attributes of built-in/extension type 'object'
# obj.__class__.__dict__.__setitem__('foo', lambda self: self.foo)
