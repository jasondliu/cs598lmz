import types
types.SimpleNamespace

s = types.SimpleNamespace()
s.name = "Jhon"
s.age = 25
s.city = "London"

print(s)
print(s.name)
print(s.age)
print(s.city)

print(s.__dict__)

# Built-in Modules

import math

print(math.pi)
print(math.sin(math.pi/2))

# Third-party Modules

# pip install camelcase
import camelcase

c = camelcase.CamelCase()
txt = 'hello world'
print(c.hump(txt))

# Create your own module

import mymodule

print(mymodule.greeting('Jhon'))

print(mymodule.person1['age'])

# Rename a Module

import mymodule as mx

print(mx.greeting('Jhon'))

# Built-in Functions

import platform

x = platform.system()
print(x)

x = dir(platform)

