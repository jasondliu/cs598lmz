from types import FunctionType
a = (x for x in [1])
b = (x for x in [1,2])
a = list(a)
b = list(b)
x = [1,2]
y = [3,4]
a = zip(x,y)
a = list(a)
print(a)
print(b)
def test(a):
    for i in a:
        print(i)
        yield i
c = test(a)
c = list(c)
# for i in c:
#     print(i)
print(c)
l = [1,2,3,4,5]
l[-1:-1:-1]


 

def test_function(a, b, c=3, *args, d, e=6, **kwargs):
    print(a, b, c, args, d, e, kwargs)

test_function(1, 2, 4, 5, 6, 7, d=8, f=9, g=10)
def func(a,b):
    return a+b
func = FunctionType(func.__code__
