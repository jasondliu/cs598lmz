fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
#fn() # TypeError: bad code object (generator)

# import dis
# dis.dis(fn)

#---------------------------------------------------------------
def fn(p=None):
    print('p =', p)

fn() # p = None
fn(p=0) # p = 0
# fn(0) # TypeError: fn() takes at most 1 positional argument (2 given)

#---------------------------------------------------------------
# def fn(a,b,c,d=None,e=None,f=None):
#     return a+b+c+d+e+f

def fn(*args,**kwargs):
    # return args[0]+args[1]+args[2]+kwargs['d']+kwargs['e']+kwargs['f']
    return sum(args)+sum(kwargs.values())

#print(fn(1,2,3)) # TypeError: fn() missing 3 required keyword-only arguments: 'd', 'e', and 'f'
print(fn(1,2,3,d=4,e=5,f=6)) #
