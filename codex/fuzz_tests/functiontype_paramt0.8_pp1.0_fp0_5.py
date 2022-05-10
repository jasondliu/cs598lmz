from types import FunctionType
list(FunctionType(code, globals(), "f"))

# @decorators.deco_2
def f(a):
    print(locals())
    print(a)


# f('hello')
a = [1, 2, 3]
print(a.__dict__)

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

# print(d.__dict__)
from collections import defaultdict

dd = defaultdict(list)
dd['hello'].append(1)
print(dd['hello'])

from collections import ChainMap

dict1 = {'name': 'tom', 'age': 123}
dict2 = {'name':'jerry', 'sex': 1}
c = ChainMap(dict1, dict2)
print(c)
print(c['name'])
print(c['age'])
print(c['sex'
