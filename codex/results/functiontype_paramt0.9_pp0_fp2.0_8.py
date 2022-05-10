from types import FunctionType
list(FunctionType())
x = lambda: 1+1
int(x)
def foo(a, b, *args):
    print args
print foo(1,2)
foo(1,2,5,5)
foo(1,2,5,5,6,7,8,9)
def bar(*args):
    print args
bar(1,2,3,4,5)
bar(1)
bar(1, 2,3,4,5,6)
def bar(*args, **kwargs):
    print 'args=', args, 'kwargs=', kwargs
bar(1,2,3,4,5)
bar(1,2,3,4,5,x=10)
bar(1,2,3,4,5,x=10,y=10)
bar(1,2,3,4,5,x=10,y=10, z=20)
bar(1,2,3,4,5,x=10,y=10, z=20, a=11,b=22,c=33,d=44)
bar
