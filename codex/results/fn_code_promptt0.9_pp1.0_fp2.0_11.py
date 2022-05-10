fn = lambda: None
# Test fn.__code__.co_flags
print("When fn is None, fn.__code__.co_flags is: ", end='')
try:
    print(fn.__code__.co_flags)
except AttributeError as err:
    print("AttributeError is raised.")
    print("Error message: " + str(err))
else:
    print("No error is raised.")

# Test fn.__code__.co_code
print("When fn is None, fn.__code__.co_code is: ", end='')
try:
    print(fn.__code__.co_code)
except AttributeError as err:
    print("AttributeError is raised.")
    print("Error message: " + str(err))
else:
    print("No error is raised.")

# Test fn.__code__.co_argcount
print("When fn is None, fn.__code__.co_argcount is: ", end='')
try:
    print(fn.__code__.co_argcount)
except AttributeError as err:
    print("AttributeError is
