import types
types.MethodType(foo, a)

# lint_ignore: E0602
a.foo = foo

# lint_ignore: E0602
a.__class__ = b


# lint_ignore: E0602
a.__class__.__bases__ = (b,)

# lint_ignore: E0602
a.__class__.__bases__ = b

# lint_ignore: E0602
a.__class__.__bases__ = (b, c)

# lint_ignore: E0602
a.__class__.__bases__ = (b, c,)

# lint_ignore: E0602
a.__class__.__bases__ = (b,)

# lint_ignore: E0602
a.__class__.__bases__ = (b, c, d)

# lint_ignore: E0602
a.__class__.__bases__ = (b, c, d,)

# lint_ignore: E0602
a.__class__.__b
