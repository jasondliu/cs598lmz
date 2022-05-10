import types
types.MethodType(func, None, A)

# This should not crash
A.__dict__['func'].__get__(None, A)

# This should not crash
A.__dict__['func'].__get__(None, A)()

# This should not crash
A.__dict__['func'].__get__(None, A)()

# This should not crash
A.__dict__['func'].__get__(None, A)()

# This should not crash
A.__dict__['func'].__get__(None, A)()

# This should not crash
A.__dict__['func'].__get__(None, A)()

# This should not crash
A.__dict__['func'].__get__(None, A)()

# This should not crash
A.__dict__['func'].__get__(None, A)()

# This should not crash
A.__dict__['func'].__get__(None, A)()

# This should not crash
A.__dict__
