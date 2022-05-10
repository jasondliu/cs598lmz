from types import FunctionType
a = (x for x in [1])
print(type(a))
b = [i for i in ['a','b']]
print(type(b))
c = map(lambda x : x, [1,2])
print(type(c.__iter__()))
d = {x : 1 for x in [1,2]}
print(type(d))
f = function(lambda x : x)
print(type(f.__code__))
e = int()
print(type(e))

if __name__ == '__main__':
    print(__name__)
