import types
# Test types.FunctionType
# Good
foo(lambda x: 2)
# PY3 Allow
foo(foo)
# PY3 Allow
foo(lambda x: x)
# Bad, asserting on non-identifier
foo(lambda foo: foo)
x = foo
# PY3 Allow, namespacing externally
type(foo)()
# PY3 Allow
foo(foo()())
# PY3 Allow
foo((lambda x, y=1: x))
# PY3 Allow
foo(lambda *x: x)
# PY3 Allow
foo(lambda **x: x)
# PY3 Allow
foo(lambda x, *y: x, y)
# PY3 Allow
foo(lambda x, **y: x, y)
# PY3 Allow
foo(lambda *x, **y: x, y)
# PY3 Allow
foo(lambda *x, **y: 1)
# PY3 Allow
lambda *x, **y: x + y
# PY3 Allow
lambda **foo: 1
# PY3 Allow
lambda *x: 1
# P
