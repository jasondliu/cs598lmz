import types
types.SimpleNamespace

#%%

class A:
    def __init__(self):
        self.x = 1
    def __getattr__(self, name):
        return f"{name} is not found"
    def __getattribute__(self, name):
        return f"{name} is not found"

a = A()
a.x

#%%

import types
a = types.SimpleNamespace()
a.x = 1
a.x

#%%

import types
a = types.SimpleNamespace(x=1)
a.x

#%%

import types
a = types.SimpleNamespace(**{"x": 1})
a.x

#%%

import types
a = types.SimpleNamespace(**dict(x=1))
a.x

#%%

import types
a = types.SimpleNamespace(**dict(x=1))
a.y

#%%

import types
a = types.SimpleNamespace(x=1)
a.y

#%%

import types

