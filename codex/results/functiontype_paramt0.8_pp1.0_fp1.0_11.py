from types import FunctionType
list(FunctionType(a,b,c,d))

#2.2
def fun(x,y):
    return x+y
x = fun(2,3)
print(x)

#2.3
def fun(x,y):
    return x+y
fun(2,3)

#2.4
def fun(x,y):
    return x+y
fun(2)

#2.5
def fun(x,y):
    return x+y
fun(2,3,4)

#2.6
def fun(x,y,z=0):
    return x+y+z
fun(2,3)

#2.7
def fun(x,y,z=0):
    return x+y+z
fun(2,3,4)

#2.8
def fun(x,y,z=0):
    return x+y+z
fun(2,3,4,5)

#2.9
def fun(x,y,z=0):
    return x+y+z

