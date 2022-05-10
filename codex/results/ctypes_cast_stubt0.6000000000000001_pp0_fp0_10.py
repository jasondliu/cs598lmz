import ctypes
ctypes.cast(id(x), ctypes.py_object).value

def f():
    a = 1
    b = 2
    c = a + b
    return c

f()

def g(x):
    def h():
        x['count'] += 1
    return h

c = {'count': 0}
action = g(c)
action()
action()
action()
c

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts

acts = makeActions()
acts[0]
acts[1]
acts[2]

acts[0](2)
acts[1](2)
acts[2](2)

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts

acts = makeActions()
acts[0]
acts[1]
acts[2]

acts[0](2)
acts[1](
