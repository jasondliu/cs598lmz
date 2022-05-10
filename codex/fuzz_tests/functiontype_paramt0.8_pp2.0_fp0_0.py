from types import FunctionType
list(FunctionType(x,globals(),'foo').__globals__)



#~ def func(x, y):
    #~ print(x,y)
#~ func(1, 2)
#~ print(func.__class__)
#~ print(type(func))
