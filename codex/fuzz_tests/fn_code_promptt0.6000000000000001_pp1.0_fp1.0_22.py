fn = lambda: None
# Test fn.__code__.co_filename
def test_fn():
    pass

def test_fn2():
    pass

test_fn.__code__.co_filename = 'Test'

print(test_fn.__code__.co_filename)
print(test_fn2.__code__.co_filename)

#Test fn.__code__.co_firstlineno
def test_fn():
    pass

def test_fn2():
    pass

print(test_fn.__code__.co_firstlineno)
print(test_fn2.__code__.co_firstlineno)

#Test fn.__code__.co_flags
def test_fn():
    pass

def test_fn2():
    pass

print(test_fn.__code__.co_flags)
print(test_fn2.__code__.co_flags)

#Test fn.__code__.co_lnotab
def test_fn():
    pass

def test_fn2():
    pass

print(test_fn.__code__
