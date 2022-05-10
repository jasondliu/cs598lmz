import types
types.MethodType(func,x)

x.count

dir(x)

x.count("world")

x.count("world",0,10)

x.count("world",-1,10)


def func(this,world):
    print("count method")
    return this.count(world,0,-1)

x.count=types.MethodType(func,x)

x.count("world")

#################

def add(this,y):
    return this + y

r=add("hello","world")

print(r)

import types

x="hello World"

types.MethodType(add,x)

x.add=types.MethodType(add,x)

x.add("world")

def func(this):
    print("method type")
    return this+"hello"

types.MethodType(func,x)

x.func=types.MethodType(func,x)

x.func()

##############################

def func(this):
    print("method
