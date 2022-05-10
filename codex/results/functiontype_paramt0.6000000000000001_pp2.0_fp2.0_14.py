from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, f.func_name, f.func_defaults, f.func_closure).func_closure)

def f():
    x = 1
    def g():
        def h():
            print x
        return h
    return g

f()()()()

def f():
    x = 1
    def g():
        def h():
            print x
        return h
    return g()

f()()()()

def f():
    x = 1
    def g():
        def h():
            print x
        return h()
    return g()

f()()()()


# f()()()()
# f()()()()

# f()()()()
# f()()()()

# f()()()()
# f()()()()

# f()()()()
# f()()()()

# f()()()()
# f()()()()

# f()()()()
# f()()()()

# f()()()()
