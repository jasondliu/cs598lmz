from types import FunctionType
a = (x for x in [1])

b = (x for x in [1,2])

# fibonacci generator
def fib():
    prev, curr= 0,1
    while True:
        yield curr
        prev, curr = curr, prev + curr

def fib_list():
    a = [0,1]
    while True:
        yield a
        a = a.append(a[-1] + a[-2])

# generator method
l = [1,2,3,4,5]
def sq(l):
    for i in l:
        yield i*i

print(sq(l))
