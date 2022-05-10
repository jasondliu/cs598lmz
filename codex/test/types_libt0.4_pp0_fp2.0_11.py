import types
types.MethodType(foo, bar)

# [3]
def foo():
    pass

def bar(x):
    return x

bar(foo)

# [4]
def foo():
    pass

def bar(x):
    return x

bar(foo())

# [5]
def foo():
    pass

def bar(x):
    return x

bar(foo)()

# [6]
def foo():
    pass

def bar(x):
    return x

bar(foo())()

# [7]
def foo():
    pass

def bar(x):
    return x

bar(foo)(x)

# [8]
def foo():
    pass

def bar(x):
    return x

bar(foo())()

# [9]
def foo():
    pass

def bar(x):
    return x

bar(foo)()

# [10]
def foo():
    pass

def bar(x):
    return x

bar(foo())


