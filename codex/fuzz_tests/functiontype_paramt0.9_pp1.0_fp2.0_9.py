from types import FunctionType
list(FunctionType(lambda xx: xx, globals(), "good_example")(x)for x in range(2))

'''

l = [10,20,30,40,50]

def f_test1(name):
    print(name)
    return name

m = map(f_test1,l)

n = map(lambda x:x*x,l)

print(list(n))
print(list(m))
