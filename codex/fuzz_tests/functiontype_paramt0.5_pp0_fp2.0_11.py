from types import FunctionType
list(FunctionType(x, globals(), 'x') for x in [lambda: None])
# [<function <lambda> at 0x7f5d5c5c5d08>]

# But that's not all...

# One of the coolest things about Python is that it's a dynamic language.
# This means that you can change the types of variables at runtime,
# and even modify the behavior of functions.

# One of the ways that Python lets you do this is through descriptors.
# A descriptor is an object that implements a method called __get__.
# Descriptors are used in a lot of places in Python,
# but the most common place you'll see them is in the property builtin.

class MyProperty:
    def __get__(self, instance, owner):
        print(f'getting {instance} {owner}')
        return 42

class MyClass:
    prop = MyProperty()

MyClass.prop
# getting None <class '__main__.MyClass'>
# 42

# The property builtin is a descriptor that implements __get__,
# __set__, and __
