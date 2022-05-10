from types import FunctionType
a = (x for x in [1])
b = lambda x: x
print(isinstance(a, FunctionType))
print(isinstance(b, FunctionType))



def func1(func):
    def func2():
        print('start')
        func()
        print('end')
    return func2

def func3():
    print('test')

test = func1(func3)
test()

print(test.__closure__)


def func1(func):
    def func2():
        print('start')
        func()
        print('end')
    return func2

@func1
def func3():
    print('test')

func3()
#func3.__closure__ == None
print(func3.__closure__)



def func1(func):
    def func2():
        print('start')
        func()
        print('end')
    return func2

@func1
def func3():
    print('test')

func3()

print(func3.__closure__)


def func1(func):
    def
