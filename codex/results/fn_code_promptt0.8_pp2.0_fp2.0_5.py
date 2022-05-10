fn = lambda: None
# Test fn.__code__.co_varnames doesn't raise AttributeError
print("Test fn.__code__.co_varnames doesn't raise AttributeError:")
try:
    for x in fn.__code__.co_varnames:
        print("x =", x)
except AttributeError as e:
    print("AttributeError:", e)

print("Test fn.__code__.co_varnames is empty:")
if fn.__code__.co_varnames:
    print("Error - fn.__code__.co_varnames is not empty")
else:
    print("fn.__code__.co_varnames is empty")

# Test variable assignment
print("Test variable assignment")
a = 1
print("a =", a)

# Test variable increment
print("Test variable increment")
a += 1
print("a =", a)

# Test variable decrement
print("Test variable decrement")
a -= 1
print("a =", a)

# Test variable multiplication
print("Test variable multiplication")
a *= 2
print
