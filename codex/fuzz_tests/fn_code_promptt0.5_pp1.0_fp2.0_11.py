fn = lambda: None
# Test fn.__code__.co_name

if fn.__code__.co_name != '<lambda>':
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_argcount

def func0(): pass
def func1(a): pass
def func2(a, b): pass

if func0.__code__.co_argcount != 0:
    print('SKIP')
    raise SystemExit

if func1.__code__.co_argcount != 1:
    print('SKIP')
    raise SystemExit

if func2.__code__.co_argcount != 2:
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_varnames

def func2(a, b): pass

if func2.__code__.co_varnames != ('a', 'b'):
    print('SKIP')
    raise SystemExit

# Test fn.__code__.co_filename

if func2.__code__.co_filename != __file__:
    print
