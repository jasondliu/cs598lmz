import gc, weakref, sys

class MyClass(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return '<MyClass: %s>' % self.name

print('Setting up objects...')
mc_ref = MyClass('mc_ref')
wr = weakref.ref(mc_ref)

# Print both objects
print('mc_ref:', mc_ref)
print('wr:', wr)

# Remove the one reference to mc_ref
del mc_ref

# Print the objects again
print('wr:', wr)

print('gc.collect():', gc.collect())

print('wr:', wr)
