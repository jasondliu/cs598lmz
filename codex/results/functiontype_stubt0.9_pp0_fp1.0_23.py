from types import FunctionType
a = (x for x in [1])
b = [1,2]
c = 'sh'
d = 1
e = {}
f = []
g = FunctionType
h = type
print('a',isinstance(a,(list,dict,tuple)))
print('b',isinstance(b,(list,dict,tuple)))
print('c',isinstance(c,(list,dict,tuple)))
print('d',isinstance(d,(list,dict,tuple)))
print('e',isinstance(e,(list,dict,tuple)))
print('f',isinstance(f,(list,dict,tuple)))
print('g',isinstance(g,(list,dict,tuple)))
print('h',isinstance(h,(list,dict,tuple)))

print(any(isinstance(n,int) for n in [1, 2, 3, 4]))
print(any(isinstance(n,int) for n in [1, 2, 3, 'a']))
print(any(isinstance(n,int) for n in [1, 2, 3, 'a
