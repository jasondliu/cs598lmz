fn = lambda: None
# Test fn.__code__.co_argcount

def f0(): pass
def f1(a): pass
def f2(a, b): pass

print(f0.__code__.co_argcount)
print(f1.__code__.co_argcount)
print(f2.__code__.co_argcount)

# Test fn.__code__.co_varnames

def f0(): pass
def f1(a): pass
def f2(a, b): pass

print(f0.__code__.co_varnames)
print(f1.__code__.co_varnames)
print(f2.__code__.co_varnames)

# Test fn.__code__.co_consts

def f0(): pass
def f1(a): pass
def f2(a, b): pass

print(f0.__code__.co_consts)
print(f1.__code__.co_consts)
print(f2.__code__.co_consts)

# Test fn
