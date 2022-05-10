fn = lambda: None
# Test fn.__code__, fn.__closure__, fn.__globals__, fn.__dict__
print(fn.__code__)
print(fn.__closure__)
print(fn.__globals__)
print(fn.__dict__)
print()

# Now with a closure
a = 10
fn = lambda: a + 1
print(fn.__closure__[0].cell_contents)
print(fn())

a = 20
print(fn.__closure__[0].cell_contents)
print(fn())

# Clear out the closure
fn.__closure__ = None
print(fn.__closure__)
print(fn())

print()
# Try a function that modifies a closure
a = 10
fn = lambda: a + 1
print(fn.__closure__[0].cell_contents)
print(fn())

print('\nChanging the closure...')
fn.__closure__[0].cell_contents += 1
print(fn.__closure__[0].cell_contents)
print(fn())

print()

