from types import FunctionType
a = (x for x in [1])
print(type(a))
print(FunctionType)
print(type(FunctionType))

def dec(func):
    def in_dec(*arg):
        print('in dec arg=',arg)
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val,int):
                return 0
        return func(*arg)
    return in_dec

@dec
def my_sum(*arg):
    return sum(arg)

@dec
def my_average(*arg):
    return sum(arg)/len(arg)

print(my_sum(1,2,3,4,5))
print(my_average(1,2,3,4,5))
print(my_sum(1,2,3,'a'))
print(my_average(1,2,3,'a'))

def my_sum2(*arg):
    return sum(arg)

def my_average2(*arg):
    return sum(arg)/len(arg)

func1 = dec(my_sum2
