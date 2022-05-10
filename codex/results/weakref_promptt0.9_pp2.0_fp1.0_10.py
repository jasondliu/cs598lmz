import weakref
# Test weakref.ref if the wrapped object when calling checkpoint() or
# savepoint() is garbage collected.
print('Test weakref')

class MyRef():
    pass

ref = weakref.ref(MyRef())
ref()

# Test if the wrapped object is garbage collected after rollback.
print('Test rollback')

# Test if the wrapped object is garbage collected after commit.
print('Test commit')
