from types import FunctionType
a = (x for x in [1])
print(a, type(a))
# print(a[0]) # 这个操作是没有意义的
print(next(a))
print(next(a))
# b = next(a)

# print(a.__next__())

def yieldtest():
    print("test")
    yield 0
    a = yield 2
    print("a=%s"%a)
    b = yield 3
    print("b=%s"%b)

# Y = yieldtest()
# print("first: " + str(next(Y)))
# print("second: " + str(next(Y)))
# print("thrid: " + str(next(Y)))
# print("fourth: " + str(next(Y)))

def yieldtest2():
    print("test2")
    yield 0
    a = yield 2
    print("a=%s"%a)
    b = yield 3
    print("b=%s"%b)

def hello():
    print("call foo()")
