fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Method call

n = 0

class A:
    def __init__(self):
        self.n = 0
    def f(self):
        self.n += 1

a = A()
a.f()
a.f()
a.f()
a.n

# Attribute access

class A:
    pass

a = A()
a.x = 1
a.x

# Function call

def f():
    return 1

f()

# Class instantiation

class A:
    def __init__(self):
        self.n = 0
    def f(self):
        self.n += 1

A()

# Import

import math
math.sin(math.pi)

# List comprehension

[x for x in range(10)]

# Generator expression

(x for x in range(10))

# Dict comprehension

{x:x for x in range(10)}

# Set comprehension

{x for x in range(10)}

#
