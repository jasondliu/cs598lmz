fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Test ellipsis in a loop
def f(x):
    l = []
    while x:
        l.append(x)
        x = x[:-1]
    return l

def g(x):
    l = []
    while x:
        l.append(x)
        x = x[:1]
    return l

def h(x):
    l = []
    while x:
        l.append(x)
        x = x[1:]
    return l

print('f', f(list(range(10))))
print('g', g(list(range(10))))
print('h', h(list(range(10))))

# Test ellipsis in a for loop
def fr(x):
    l = []
    for i in x:
        l.append(i)
        x = x[:-1]
    return l

def gr(x):
    l = []
    for i in x:
        l.append(i)
        x = x[:1]
   
