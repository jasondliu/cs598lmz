import types
types.SimpleNamespace

#%%
import types
class MyNamespace(types.SimpleNamespace):
    def __str__(self):
        return 'my namespace'

#%%
class MyNamespace(types.SimpleNamespace):
    def __str__(self):
        return 'my namespace'

a = MyNamespace()
a.b = 1
a.c = 2

a

#%%
a.__dict__

#%%
a.__dir__()

#%%
class MyNamespace(types.SimpleNamespace):
    def __str__(self):
        return 'my namespace'

a = MyNamespace()
a.b = 1
a.c = 2

a
a.__dict__

#%%
a
a.__dir__()

#%%
a
a.__dir__()

#%%
a
a.__dir__()

#%%
a
a.__dir__()

#%%
a
a.__dir__()

#%%
a
a.__dir__()


