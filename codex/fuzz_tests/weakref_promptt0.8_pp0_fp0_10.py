import weakref
# Test weakref.ref(callable) raises a typeerror
try:
    weakref.ref(lambda: None)
except TypeError:
    pass
else:
    print("failed to raise typeerror")
