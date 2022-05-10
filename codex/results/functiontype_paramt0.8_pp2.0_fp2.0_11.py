from types import FunctionType
list(FunctionType(a).__code__.co_freevars)

('d',)

# fn.__code__.co_freevars
# (fn.__code__.co_names + fn.__closure__) if fn.__closure__ else fn.__code__.co_names

# >>> list(FunctionType(b).__code__.co_names)
# ['d', 'b', 'e']
# >>> list(FunctionType(b).__code__.co_freevars)
# ['d', 'e']
