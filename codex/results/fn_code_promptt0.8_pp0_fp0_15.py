fn = lambda: None
# Test fn.__code__
print(fn.__code__)
print(fn.__code__.co_filename)
print(fn.__code__.co_name)
print(fn.__code__.co_argcount)


def fn2(x, y):
    a, b = x, y

# __code__.co_varnames
print(fn2.__code__.co_varnames)

# __code__.co_consts
print(fn2.__code__.co_consts)

# __code__.co_freevars
def fn3(x, y):
    a = x
    b = y
    def fn4():
        return a + b

print(fn3.__code__.co_freevars)

# __code__.co_closure
print(fn3.__code__.co_closure)

# __code__.co_cellvars
def fn5():
    a = 1
    def fn6():
        a = 2
        print(a)
    fn6()

print(fn
