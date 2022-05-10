fn = lambda: None
# Test fn.__code__.co_varnames

def f1(a,b,c):
    pass

def f2(a,b,c=4):
    pass

def f3(a,b=4,c=5):
    pass

def f4(a=4,b=5,c=6):
    pass

def f5(a,b,*c):
    pass

def f6(a,b,*c,**d):
    pass

def f7(a,b,*c,d=4,**e):
    pass

def f8(a,b,*c,d=4,e=5,**f):
    pass

def f9(a,b,*c,d=4,e=5,**f):
    g = 4

def f10(a,b,*c,d=4,e=5,**f):
    g = 4
    def h():
        pass

def f11(a,b,*c,d=4,e=5,**f):
   
