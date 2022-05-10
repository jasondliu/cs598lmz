from types import FunctionType
list(FunctionType(a).__globals__.values())[0].eval('2+2')
</code>
or (2):
<code>class Wrap:
    def __init__(self, f):
        self.f = f
    def __call__(self, *args, **kwargs):
        res = self.f(*args, **kwargs)
        print(self.f.__globals__)
        return res
        

@Wrap
def f(a):
    return a

f(2)
</code>

