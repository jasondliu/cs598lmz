fn = lambda: None
# Test fn.__code__.co_flags
x.fn.__code__.co_flags
# Test fn.__code__.co_consts
x.fn.__code__.co_consts
# Test fn.__code__.co_stacksize
x.fn.__code__.co_stacksize
# Test fn.__code__.co_varnames
x.fn.__code__.co_varnames

x = MyClass()

# BEGIN TEST FOR PYTHON-2736
try:
    x.fn2
finally:
    x.fn
# END TEST FOR PYTHON-2736

# BEGIN TEST FOR PYTHON-2736
x.fn2
# END TEST FOR PYTHON-2736

# Module attribute invalidation
# ============================================================

m = types.ModuleType("m")
m.x = 1
m.y = 2

# BEGIN TEST FOR PYTHON-2557
m2 = types.ModuleType("m2")
m2.x = 3
m2.y =
