from types import FunctionType
list(FunctionType(lambda:0,{},None,None))

print(list(FunctionType(lambda:0,{},None,None)))

#map(function,iterable,...)

print(list(map(lambda x:x+1,[1,2,3,4,5])))

print(list(map(lambda x:x**2,(1,2,3,4,5))))

#reduce(function,iterable[,initializer])

def add(x,y):
    return x+y

print(reduce(add,[1,2,3,4,5]))

def acm(x,y):
    return x*10+y

print(reduce(acm,[1,2,3,4,5]))

#filter(function or None,iterable)

print(list(filter(None,[1,0,False,True])))

print(list(filter(lambda x:x>2,[1,2,3,4,5,6,7])))

#sorted(iterable,cmp=None,
