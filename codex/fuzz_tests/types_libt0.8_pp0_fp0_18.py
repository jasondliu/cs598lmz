import types
types.ClassType

#-------------------------------------------------------------------------------

#!/usr/bin/python

import types

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

for (name,thing) in types.__dict__.items():
    if type(thing) == types.ClassType:
        print name

#-------------------------------------------------------------------------------

#!/usr/bin/python

import types

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

myobj = MyClass()
for (name,thing) in types.__dict__.items():
    if type(thing) == types.ClassType:
        print name, '::', thing.im_func

#-------------------------------------------------------------------------------

#!/usr/bin/python

import types

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

myobj = MyClass()
for (name,
