from types import FunctionType
list(FunctionType(x(3,4),g).__code__.co_varnames)

def x(a,b,c=1,d=2,*args,**kwargs):
    return a+b+c+d
x(1,1,1,1,1,1,1,1,e=6,f=6,h=6)




def add(x,y):
    return x+y
    
add(1,1)

def add(x,*args):
    total = x
    for arg in args:
        total += arg
    return total

def x(a,b,c=3):
    return a+b+c
x(2,3,4)

def x(a,b,c=3,*args,**kwargs):
    pass

x(2,3,4,5,6,7,d=1,e=2)

def x(a,b,c=1,d=2,*args):
    print(a,b,c,d,args)
x(2,
