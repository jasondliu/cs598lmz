gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_NOFREE)

def f(): pass
print(f.__code__.co_flags & inspect.CO_NOFREE)

def f(): pass
def g(a=f): pass

def h(): pass
h.attr = f

def i(): pass
i.attr = (f,)

def j(): pass
j.attr = {f:1}

def k(): pass
k.attr = [f, h]

def l():
    x = (g, h, i, j, k)
print(l.__code__.co_nfreevars)
print(l.__closure__)

print(l.__code__.co_flags & inspect.CO_NOFREE)
print(l.__closure__[0].cell_contents.__code__.co_flags & inspect.CO_NOFREE)
print(l.__closure__[1].cell_contents.__code__.co_flags & inspect.CO_NOFREE)
print(l
