fn = lambda: None
# Test fn.__code__.co_name

def some_fn(): pass
fn = some_fn
try:
    fn.__code__.co_name
except AttributeError:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_argcount

def t1(): pass
def t2(a): pass
def t3(a, b): pass

print('t1', t1.__code__.co_argcount)
print('t2', t2.__code__.co_argcount)
print('t3', t3.__code__.co_argcount)

# Test fn.__code__.co_varnames

def t1(): pass
def t2(a): pass
def t3(a, b): pass

print('t1', t1.__code__.co_varnames)
print('t2', t2.__code__.co_varnames)
print('t3', t3.__code__.co_varnames)

# Test fn.__code__.co_arg
