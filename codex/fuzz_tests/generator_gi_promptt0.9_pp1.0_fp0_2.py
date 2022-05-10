gi = (i for i in ())
# Test gi.gi_code

def g(x, y):
    print(x, y)

print(g(1, g))
print(g(1, g(2, 3)))
print(g(1, g(2, 3) + 10))

def f(x, y, z, g=0):
    print(x, y, z, g)
print(f(1, g, f))
print(f(g, f, g, 1))

# Test __new__ and __init__

class C(object):
    def __new__(cls, x):
        print('C().__new__(', x, ')')
        return object.__new__(cls)

    def __init__(self, x):
        print('C().__init__(', x, ')')

c = C('argument for constructor')
print(c)

def f(x):
    print('f called with', x)

f(4)

class G(object):
    def g(self):
        print('G.g')

def
