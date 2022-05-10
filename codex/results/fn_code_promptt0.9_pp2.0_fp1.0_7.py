fn = lambda: None
# Test fn.__code__
try:
    fn.__code__ = 'x'
except Exception as e:
    print('SKIP')
    import sys
    sys.exit()

def fn1():
    pass

def fn2():
    return

print('no args')
print(fn1.__code__.co_argcount)
print('no args, no return statement')
print(fn2.__code__.co_argcount)
