import types
types.ClassType

# This is one method of creating a class.
class FooBar:
    'my very first class: FooBar'
    version = 0.1 # class (data) attribute

print FooBar.__doc__
print '-'*50
help(FooBar)
print '-'*50
f = FooBar()
print f
