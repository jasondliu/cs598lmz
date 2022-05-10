fn = lambda: None
# Test fn.__code__ is None

# Exercise 1:
print("-" * 80)
print("Exercise 1")
print("-" * 80)

print(fn.__code__ is None)

# output:
# ----------------------------------------
# Exercise 1
# ----------------------------------------
# True

# Exercise 2:
print("-" * 80)
print("Exercise 2")
print("-" * 80)

from types import FunctionType

def my_decorator(fn):
    def wrapper(*args, **kwargs):
        print("from my decorator")
        print("from my decorator", fn.__code__, fn.__code__ is None)
        fn(*args, **kwargs)
    return wrapper

@my_decorator
def print_hello():
    print("from print_hello")

print("from outside", print_hello.__code__, print_hello.__code__ is None)
print("from outside", FunctionType, print_hello.__class__ == FunctionType)

print_hello()

# output:
# ----------------------------------------
# Exercise 2
# ----------------------------------------

