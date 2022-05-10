import types
types.MethodType(method, arg)
</code>
This however doesn't work in python 3 anymore. 
What is the new way to do this?


A:

You can do something like this:
<code>#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A():
    def __init__(self):
        self.bar = lambda x: self.foo(x)

    def foo(self, x):
        return x+1

a = A()
print a.bar(2)
</code>

