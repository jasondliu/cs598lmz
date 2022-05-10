from types import FunctionType
list(FunctionType(f.__code__,f.__globals__,name=f.__name__,
                  argdefs=f.__defaults__,closure=f.__closure__)
     for f in (lambda x,y=10,*z: x+y+sum(z), lambda x,y=10,*z,**w: x+y+sum(z)+sum(w.values())))

# [(2, 3, 4, 5), (2, 3, 4, 5)]
# [(2, 3, 4, 5), (2, 3, 4, 5), (2, 3, 4, 5)]
# [(2, 3, 4, 5), (2, 3, 4, 5), (2, 3, 4, 5), (2, 3, 4, 5)]
