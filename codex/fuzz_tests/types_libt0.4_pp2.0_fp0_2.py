import types
types.SimpleNamespace

#%%

from collections import namedtuple

#%%

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
p[0] + p[1]

#%%

x, y = p
x, y

#%%

p.x + p.y

#%%

p

#%%

p = Point(x=11, y=22)
p

#%%

p[0] + p[1]

#%%

x, y = p
x, y

#%%

p.x + p.y

#%%

p

#%%

p = Point(11, 22)
p

#%%

p[0] + p[1]

#%%

x, y = p
x, y

#%%

p.x + p.y

#%%

p

#%%

p = Point(11, y=22)
p

#%%

p[0
