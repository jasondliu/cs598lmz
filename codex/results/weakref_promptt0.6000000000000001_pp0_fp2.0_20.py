import weakref
# Test weakref.ref()

from test import support
import gc, weakref

class TestObject:
    pass

obj = TestObject()

# Test weakref.ref()
w = weakref.ref(obj)

# Test weakref()
w = weakref.WeakValueDictionary()
w['obj'] = obj

# Check that the objects are still alive
print(obj)
print(w['obj'])

# Check that the objects are still alive
print(obj)
print(w['obj'])

# Check that the objects are still alive
print(obj)
print(w['obj'])

# Check that the objects are still alive
print(obj)
print(w['obj'])

# Check that the objects are still alive
print(obj)
print(w['obj'])

# Check that the objects are still alive
print(obj)
print(w['obj'])

# Check that the objects are still alive
print(obj)
print(w['obj'])

# Check that the objects are still alive
print(obj)
print(w['
