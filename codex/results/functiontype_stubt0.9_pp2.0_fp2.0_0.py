from types import FunctionType
a = (x for x in [1])
# a.send(5)

def gen(input):
    while True:
        init = yield
        print(input, init)

gen_t = gen(5)
gen_t.send(None)
gen_t.send(1)

a = 5 if 6 else 7

class A(object):
    def __init__(self):
        pass

# a = A()
# a()

class Singleton(object):
    __instance = None
    def __new__(cls,*args, **kwd):
        if not cls.__instance :
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

test1 = Singleton()
test2 = Singleton()
print(test1 is test2)
print(test1,test2)
print(id(test1),id(test2))

print([i for i in range(5) if i>2])

a = '123'
id(a)
a
