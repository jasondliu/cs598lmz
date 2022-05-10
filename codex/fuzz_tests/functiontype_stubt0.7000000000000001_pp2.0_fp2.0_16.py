from types import FunctionType
a = (x for x in [1])
b = [lambda:print('b'),lambda:print('c')]
print(type(a),type(b))


#isinstance()
a = [1,2,3]
b = (1,2,3)
c = int(12)
print(isinstance(a,list))
print(isinstance(b,list))
print(isinstance(b,list))
print(isinstance(c,list))


#issubclass()
class A(object):
    pass
class B(A):
    pass
print(issubclass(B,A))
print(issubclass(A,B))
print(issubclass(A,object))
print(issubclass(object,object))
print(issubclass(bool,int))
print(issubclass(float,int))
print(issubclass(bool,object))


#iter()
a = [1,2,3]
b = iter(a)
print(type(a),type(b))
print(next(b))
print(next(b))
print(next(
