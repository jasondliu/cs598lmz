import weakref
# Test weakref.ref(int) exception (#2827)
try:
    weakref.ref(int)
except TypeError: pass
else:
    print('Failed')
    import sys
    sys.exit(1)

print('Passed')
