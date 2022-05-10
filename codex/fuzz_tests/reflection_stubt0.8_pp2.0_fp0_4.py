fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
tuple(fn())
'''

'''
class A:
    def f(*args):
        print(args)
class B(A): pass
def f(*args):
    print(args)

B.f('b')
'''

# dir(__builtins__)

'''
x = type(y)
print(x)
y = 1
print(x)
'''
