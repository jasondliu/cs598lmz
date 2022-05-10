from types import FunctionType
list(FunctionType(lambda x: None, {}, "test", (int, str,), None).__closure__)

# __code__
list(lambda x: None.__code__.co_freevars)
list(lambda x: None.__code__.co_cellvars)
list(lambda x: None.__code__.co_varnames)

# tests for inspect.getclosurevars()
def nested_func():
    a = 1
    def inner_func():
        nonlocal a
        def really_inner_func():
            a = 1
            print(a)
        really_inner_func()
    inner_func()
nested_func()

def nested_func2():
    a = 1
    def inner_func2():
        nonlocal a
        def really_inner_func2():
            a = 1
            print(a)
        return really_inner_func2
    return inner_func2

x = nested_func2()()
inspect.getclosurevars(x)

def nested_func3():
    a = 1

