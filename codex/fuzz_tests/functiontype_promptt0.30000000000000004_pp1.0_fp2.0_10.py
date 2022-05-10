import types
# Test types.FunctionType and types.LambdaType

def f(): pass

class C:
    def g(self): pass

def h(a, b, c): return a+b+c

def i(a, b, c, d=1, e=2): return a+b+c+d+e

def j(a, b, c, d=1, e=2, *f): return a+b+c+d+e+f[0]

def k(a, b, c, d=1, e=2, *f, **g): return a+b+c+d+e+f[0]+g['x']

def l(a, b, c, d=1, e=2, *f, **g): return a+b+c+d+e+f[0]+g['x']+g['y']

def m(a, b, c, d=1, e=2, *f, **g): return a+b+c+d+e+f[0]+g['x']+g['y']+g['z
