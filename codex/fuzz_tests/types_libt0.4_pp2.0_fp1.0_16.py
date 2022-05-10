import types
types.SimpleNamespace(a=1, b=2, c=3)

#%%

import types
types.SimpleNamespace(**{'a': 1, 'b': 2, 'c': 3})

#%%

import types
types.SimpleNamespace(**dict(a=1, b=2, c=3))

#%%

import types
types.SimpleNamespace(**dict(zip(['a', 'b', 'c'], [1, 2, 3])))

#%%

import types
types.SimpleNamespace(**dict(zip('abc', [1, 2, 3])))

#%%

import types
types.SimpleNamespace(**dict(zip('abc', (1, 2, 3))))

#%%

import types
types.SimpleNamespace(**dict(zip('abc', {1, 2, 3})))

#%%

import types
types.SimpleNamespace(**dict(zip('abc', {1, 2, 3})))

#%%

import types
types.SimpleNamespace(**dict(zip('
