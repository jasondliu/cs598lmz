from types import FunctionType
a = (x for x in [1])
print(type(a))
print(type(lambda a: a))
print(type((lambda a: a)))
print(type(FunctionType))


# 无参数装饰器
def dec(func):
    def wrapper(*args, **kwargs):
        print('c2')
        res = func(*args, **kwargs)
        print('a2')
        return res

    print('b2')
    return wrapper


# 有参数装饰器
def dec2(argv):
    def wrapper1(func):
        def wrapper2(*args, **kwargs):
            print('a1')
            res = func(*args, **kwargs)
            print('c1')
            return res

        print('b1')
        return wrapper2

    return wrapper1


@dec2(123)
def test():
    print('test func')


test()

test2 = dec(test)
test2()


# 链式装饰器
def dec
