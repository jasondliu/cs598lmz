from types import FunctionType
a = (x for x in [1])
type(a)

a
b = [x for x in [1]]
type(b)
b
c = {x for x in [1]}
type(c)
c
d = {x: x for x in [1]}
type(d)
d
e = 'abc'
type(e)
e
f = b'abc'
type(f)
f
g = FunctionType
type(g)
g
h = property
type(h)
h
i = classmethod
type(i)
i
j = staticmethod
type(j)
j

# 注意：不要对实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属
