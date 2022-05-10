fn = lambda: None
# Test fn.__code__.co_freevars
def freevars1():
    freevars2()
freevars1.__code__.co_freevars

# Test fn.__closure__
def freevars2():
    print(x)
x = 100
freevars1.__closure__
freevars1.__closure__[0].cell_contents
freevars2()

# Test fn.__code__.co_consts
def consts():
    pass
consts.__code__.co_consts

# Test fn.__code__.co_varnames
def varnames():
    a = b = 0
    c, *d = e = ()
    for f in g:
        g = h(i)
        j = lambda k=l: m(n)
varnames.__code__.co_varnames

# Test fn.__code__.co_filename
def filename():
    pass
filename.__code__.co_filename

# Test fn.__code__.co_name
def name():
    pass
