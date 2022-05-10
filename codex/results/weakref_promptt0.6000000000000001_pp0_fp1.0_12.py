import weakref
# Test weakref.ref(1):
assert weakref.ref(1)() == 1

# Test weakref.ref(sys.stdout):
import sys
assert weakref.ref(sys.stdout)() is sys.stdout

# Test weakref.ref(sys.stdout.write):
assert weakref.ref(sys.stdout.write)() is sys.stdout.write

# Test weakref.ref(sys.stdout.write, ...):
assert weakref.ref(sys.stdout.write, lambda x: None)() is sys.stdout.write

# Test weakref.ref(sys.exit):
assert weakref.ref(sys.exit)() is sys.exit

# Test weakref.ref(sys.exit, ...):
assert weakref.ref(sys.exit, lambda x: None)() is sys.exit

# Test weakref.ref(sys.exit, ...) after calling it:
w = weakref.ref(sys.exit, lambda x: None)
assert w() is sys.exit
print(w())

# Test weakref.ref
