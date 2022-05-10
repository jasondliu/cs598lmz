fn = lambda: None
# Test fn.__code__.co_varnames
class A(object):
    def f(self, a, b=1, c=2, *args):
        pass
fn = A().f
assert fn.__code__.co_varnames == ('self', 'a', 'b', 'c', 'args')
assert fn.__code__.co_argcount == 3
# Test fn.__defaults__
assert fn.__defaults__ == (1, 2)
# Test fn.__globals__, fn.__closure__
def f(): pass
def g(): pass
def h(): f.attr = True
assert f.__globals__ is globals()
assert f.__closure__ == None
h.__closure__

def f(a):
    print(a)
    x = 1
    def g(b):
        print(b)
        print(x)
    g(a*10)
f(3)

def f(a):
    print(a)
    x = [1]
    def g(b):
        print(b)
       
