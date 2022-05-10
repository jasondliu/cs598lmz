from types import FunctionType
list(FunctionType(lambda:0,{}).__code__.co_varnames)

a,*b,c=range(5)
#[0, 1, 2, 3, 4]
a
#0
b
#[1, 2, 3]
c
#4

a,*b=range(5)
#[0, 1, 2, 3, 4]
a
#0
b
#[1, 2, 3, 4]

a,b,*c=range(5)
#[0, 1, 2, 3, 4]
a
#0
b
#1
c
#[2, 3, 4]

a,b,c,*d=range(5)
#[0, 1, 2, 3, 4]
a
#0
b
#1
c
#2
d
#[3, 4]

#*a,b=range(5)
#SyntaxError: starred assignment target must be in a list or tuple

#a,b,*c,d=range(5)
#SyntaxError:
