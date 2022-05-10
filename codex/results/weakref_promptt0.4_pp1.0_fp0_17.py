import weakref
# Test weakref.ref(obj)
def foo(obj):
    print(obj)

obj = object()
ref = weakref.ref(obj, foo)
print(ref)
print(ref())
print(obj)

# Test weakref.ref(obj, callback)
def bar(obj):
    print(obj)

obj = object()
ref = weakref.ref(obj, bar)
print(ref)
print(ref())
print(obj)

# Test weakref.ref(obj, callback) with callback None
obj = object()
ref = weakref.ref(obj, None)
print(ref)
print(ref())
print(obj)

# Test weakref.ref(obj, callback) with callback not callable
def baz(obj):
    print(obj)

obj = object()
try:
    ref = weakref.ref(obj, baz)
except TypeError:
    print("TypeError")

# Test weakref.ref(obj, callback) with callback not callable
obj = object()
try:
    ref = weakref.ref(
