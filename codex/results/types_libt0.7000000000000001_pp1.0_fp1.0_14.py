import types
types.SimpleNamespace

x = types.SimpleNamespace(name='John', age=22)

x

print(x.name)
print(x.age)

y = types.SimpleNamespace(**dict(name='John', age=22))
y

print(y.name)
print(y.age)

z = types.SimpleNamespace(**dict(name='John', age=22, weight=x))
z

z.weight

z.weight.age

z.weight.age = 99
z.weight.age

x.age

z.weight = x
z.weight.age

x.age = 33
z.weight.age

x.age = 22
z.weight.age

#%%

import types

def make_object(**kwargs):
    return types.SimpleNamespace(**kwargs)

x = make_object(name='John', age=22)
x

print(x.name)
print(x.age)

#%%

import collections

collections.namedt
