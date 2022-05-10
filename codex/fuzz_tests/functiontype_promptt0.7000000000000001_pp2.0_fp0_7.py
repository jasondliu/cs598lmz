import types
# Test types.FunctionType
def f(x):
    return x
class C:
    def f(self):
        return "f"
    def g(self, x):
        return "g"
    def h(self, x, y):
        return "h"
    def i(self, x, y, z):
        return "i"
    def m(self, a=1, b=2, c=3):
        return "m"
    def n(self, a=1, b=2, c=3, d=4):
        return "n"
    def o(self, a=1, b=2, c=3, d=4, e=5):
        return "o"
    def p(self, a=1, b=2, c=3, d=4, e=5, f=6):
        return "p"
    def q(self, a=0, b=0, c=0, d=0, e=0, f=0, g=0):
        return "q"
    def r(self, a=0, b
