fn = lambda: None
# Test fn.__code__ 1
try:
    assert(fn.__code__.co_argcount == 0)
except AssertionError:
    print('1)', end='')
    read_input()

# Test fn.__code__ 2
try:
    assert(fn.__code__.co_nlocals == 1)
except AssertionError:
    print('2)', end='')
    read_input()

# Test fn.__code__ 3
try:
    assert(fn.__code__.co_varnames == ('fn',))
except AssertionError:
    print('3)', end='')
    read_input()

# Test fn.__code__ 4
try:
    assert(fn.__code__.co_flags & (~0x0ffff))
except AssertionError:
    print('4)', end='')
    read_input()

# Test fn.__closure__
try:
    assert(fn.__closure__ is None)
except AssertionError:
    print('5)', end=''
