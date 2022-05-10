from types import FunctionType
list(FunctionType(lambda x: x+1, globals())(2))

def f(x):
    return x+1
list(f(2))

# 3.3.3
def f(x):
    def g(y):
        return y+x+3
    return g
nf1 = f(1)
nf2 = f(3)
nf1(1)
nf2(1)

# 3.3.4
def f(x):
    def g(y):
        return y+x+3
    return g
nf1 = f(1)
nf2 = f(3)
nf1(1)
nf2(1)

# 3.3.5
def polynomial(coeffs):
    def p(x):
        total = 0
        for i, c in enumerate(coeffs):
            total += c * x**i
        return total
    return p
p1 = polynomial([1, 2, 3])
p2 = polynomial([3, 2, 1])
p1
