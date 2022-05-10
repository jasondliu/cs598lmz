import weakref
# Test weakref.ref(str) exception
try:
    weakref.ref(str)
except:
    pass
