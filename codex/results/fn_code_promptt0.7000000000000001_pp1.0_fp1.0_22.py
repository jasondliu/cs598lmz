fn = lambda: None
# Test fn.__code__.co_varnames

def f0():
    return 1
def f1(a):
    return 1
def f2(a=1):
    return 1
def f3(a,b):
    return 1
def f4(a=1,b=2):
    return 1
def f5(a=1,b=2,c=3):
    return 1
def f6(a,b,c=3,d=4):
    return 1
def f7(a,b,c=3,d=4,e=5):
    return 1
def f8(a,b,c=3,d=4,e=5,f=6):
    return 1
def f9(a,b,c=3,d=4,e=5,f=6,g=7):
    return 1
def f10(a,b,c=3,d=4,e=5,f=6,g=7,h=8):
    return 1
def f11(a,b,c=3,d=4,e=
