gi = (i for i in ())
# Test gi.gi_code.co_flags
class G:
    def meth(self):
        pass

    def genmeth(self):
        yield 1

    @classmethod
    def cmeth(cls):
        pass

    @staticmethod
    def smeth():
        pass

    async def ameth(self):
        pass

    async def agenmeth(self):
        yield 1

# test gi.gi_code.co_argcount
def f0():
    pass

def f1(a):
    pass

def f2(a, b):
    pass

def f3(a, b, c):
    pass

def f4(a, b, c, d):
    pass

def f5(a, b, c, d, e):
    pass

def f6(a, b, c, d, e, f):
    pass

def f7(a, b, c, d, e, f, g):
    pass

def f8(a, b, c, d, e, f, g, h):
   
