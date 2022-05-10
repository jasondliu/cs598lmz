import ctypes
ctypes.cast(id(x), ctypes.py_object).value

#%%
# Dictionaries
#%%
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
tel['jack']
del tel['sape']
tel['irv'] = 4127
tel
list(tel)
sorted(tel)
tel['jack']
'guido' in tel
#%%
# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
#%%
# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
{x: x**2 for x in (2, 4, 6)}
#%%
# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
dict(sape=4139, guido=4127, jack=4098)
#%%
# Looping Techniques
#%%
knights = {'gallahad': 'the pure', 'ro
