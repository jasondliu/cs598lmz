gi = (i for i in ())
# Test gi.gi_code.co_filename
print(gi.__code__.co_filename)
print()

# Test def
def func(): pass
print(func.__name__)
print(func.__code__.co_filename)
print(func.__code__.co_firstlineno)
print()

# Test lambda
f = lambda: print((1,))
print(f.__code__.co_filename)
print(f.__code__.co_firstlineno)
print()

# Test for
for i in (): pass
print()

# Test class
class foo: pass
print()
