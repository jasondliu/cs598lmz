import weakref
# Test weakref.ref() function

# See http://effbot.org/zone/python-weak-references.htm
class Foo():

    def __init__(self, name):
        self.name = name

    def __del__(self):
        pass
        print('Deleting {}'.format(self))

    def __repr__(self):
        return '<Instance of Foo named {!r} at {:#x}>'.format(
            self.name, id(self))

a = Foo('duck')
weak_a = weakref.ref(a)
print('Before:', weak_a)
print('a:', a)

# create another reference directly - this doesn't update the weakref
b = a

# update the weakref by creating another object
a = None
print('After:', weak_a)
