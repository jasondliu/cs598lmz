from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, 'x', f.func_defaults, f.func_closure).func_closure)

def f():
    a = 1
    def g():
        return a
    return g
f()()
p = f()
p.func_closure
p.func_closure[0]

def f():
    a = 1
    def g(x):
        return a + x
    return g
p = f()
p(2)

def f():
    a = []
    def g(x):
        a.append(x)
        return a
    return g
p = f()
p(1)
p(2)
p(3)
p(4)

def f():
    a = []
    def g(x):
        def h():
            a.append(x)
            return a
        return h
    return g
p = f()
p(1)
p(2)
p(3)
p(4)

def f():
    a = []
   
