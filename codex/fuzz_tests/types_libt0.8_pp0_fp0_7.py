import types
types.ClassType
"""
>>> int()
0
>>> bool()
False
>>> float()
0.0
>>> dict()
{}
>>> list()
[]
>>> set()
set()
>>> tuple()
()
>>> str()
''
>>> type({})
<class 'dict'>
"""
"""
>>> Dict = dict
>>> Dict()
{}
>>> Dict(['a'])
{'a': None}
>>> Dict({'a': 1})
{'a': 1}
>>> Dict(zip(['a', 'b'], [1, 2]))
{'a': 1, 'b': 2}
>>> d = {'a': 1}
>>> dict(d) is d
True
>>> dict(d, **d)
{'a': 1}
>>> dict([d], **d)
{'a': 1}
>>> dict(dict(d), **d)
{'a': 1}
>>> dict(d, **dict(d))
{'a': 1}
>>> dict(**d) is d
True
>>> dict(**d
