gi = (i for i in ())
# Test gi.gi_code.co_firstlineno
print(foo.gi.gi_code.co_firstlineno)
# Test gi.gi_frame.f_lineno
print(foo.gi.gi_frame.f_lineno)

# Test try/finally
def foo():
    try:
        print('foo')
    finally:
        print('finally')

foo()

# Test try/except/finally
def foo():
    try:
        print('foo')
    except TypeError:
        print('TypeError')
    finally:
        print('finally')

foo()

# Test try/except/else/finally
def foo():
    try:
        print('foo')
    except TypeError:
        print('TypeError')
    else:
        print('else')
    finally:
        print('finally')

foo()

# Test try/except/else/finally/else
def foo():
    try:
        print('foo')
    except TypeError:
        print('TypeError')
    else:
        print('
