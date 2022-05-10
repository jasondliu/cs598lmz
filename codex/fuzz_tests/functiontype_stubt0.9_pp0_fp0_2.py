from types import FunctionType
a = (x for x in [1])
print(isinstance(a,FunctionType))
b = (x for x in [1])
print(isinstance(b,FunctionType))
print(isinstance(None,FunctionType))

'''
for x in range(3):
    def f():
        return x
    print(f())
'''

print("-----------------------------------")

def g():
    l = []
    for x in range(3):
        def f():
            return x
        l.append(f)
    return l

h = g()
print(type(h))
print(h[0])
print(h[1])
print(h[2])
print(h[0]())
print(h[1]())
print(h[2]())

print("-----------------------------------")

def prt(s):
    print("g:",s)
    return s

b = prt("Hi")
print("b:",b)

def g1(s):
    s = s + " world"
    print("g1:",s)
    return s
