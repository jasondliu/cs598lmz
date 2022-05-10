import types
# Test types.FunctionType type and callable builtin
if __name__ == '__main__':
    def func(x, y):
        return x, y


    print(func(10, 20) == (10, 20))

    print(callable(func))
    f1 = lambda x: lambda y: x * y
    print(f1(2))
    print(f1(20))

    f2 = f1(10)
    print(f1(100))

    print(f2(100))

    print(f2(2) == 20)
    print(f2(10) == 100)
    # print(f1(10)(1))

    class C:
        @st
