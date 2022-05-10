from types import FunctionType
list(FunctionType(Function) is Function)

# next, prev
@Function(1, 1)
def next(a):
    if isinstance(a, Iterable): return iter(a).next()
    b = []
    for _ in a: b.append(_)
    return b[0]

@Function(1, 1)
def prev(a):
    if isinstance(a, Iterable):
        i = iter(a)
        p = next(i)
        for n in i: p = n
        return p
    b = []
    for _ in a: b.append(_)
    return b[-1]

# rest, init
@Function(1, 1)
def rest(a):
    if isinstance(a, Iterable): return chain(next(iter(a)), a)
    return a[1:]

@Function(1, 1)
def init(a):
    if isinstance(a, Iterable):
        i = iter(a)
        p = next(i)
        for n in i: p = n
        return chain(iter
