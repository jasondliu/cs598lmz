import weakref
# Test weakref.ref() called with an object that has __del__.
# Expecting an error message when __del__ is called, since object
# is not tracked.
class X:

    def __del__(self):
        print('X.__del__')
        self.x = 1

print('Calling ref()')
r = weakref.ref(X())
print('Done calling ref')
