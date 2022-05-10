from types import FunctionType
list(FunctionType(add.__code__, {}))

# --

def add(a, b):
    return a + b

print(add.__code__)
print(add.__code__.co_varnames)
print(add.__code__.co_argcount)

# --

def make_adder(n):
    def adder(k):
        return k + n
    return adder

add_10 = make_adder(10)
add_20 = make_adder(20)

print(add_10(10))
print(add_20(10))
print(add_10.__code__ == add_20.__code__)

# --

class Adder:
    def __init__(self, n):
        self.n = n
    
    def __call__(self, k):
        return k + self.n

add_10 = Adder(10)
add_20 = Adder(20)

print(add_10(10))
print(add_20(10))
print(add_10.
