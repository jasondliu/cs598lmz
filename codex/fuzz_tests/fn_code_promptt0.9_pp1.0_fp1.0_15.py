fn = lambda: None
# Test fn.__code__.co_flags and CO_NOFREE
print(o.__code__.co_flags & o.CO_NOFREE)
print(f.__code__.co_flags & o.CO_NOFREE)
print(g.__code__.co_flags & o.CO_NOFREE)
print(t.__code__.co_flags & o.CO_NOFREE)
print(fn.__code__.co_flags & o.CO_NOFREE)
# Same for get_code.co_flags
print(o.__code__.co_flags & o.CO_NOFREE)
print(f.__code__.co_flags & o.CO_NOFREE)
print(g.__code__.co_flags & o.CO_NOFREE)
print(t.__code__.co_flags & o.CO_NOFREE)
print(fn.__code__.co_flags & o.CO_NOFREE)
# Clear CO_NOFREE flag
o.__code__ = o.__code__.replace(co_flags = o.__code__.co_
